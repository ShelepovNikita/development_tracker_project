import random

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.v1.serializers import (
    CourseSerializer,
    PatchUserSkillSerializer,
    SelectionSerializer,
    SkillSerializer,
    UserDataSkillSerializer,
    UserSkillSerializer,
)
from api.v1.viewsets import ListViewSet
from courses.models import Course
from skills.models import Skill
from selections.models import Selection
from users.models import CustomUser, UserSkill


class RecommendedCoursesTrackerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Возвращает рекомендованные курсы на основе хотя бы одного
        совпадения навыка пользователя с курсом, который он еще не проходил
        для страницы Трекер."""

        user = get_object_or_404(CustomUser, id=self.request.user.id)
        user_courses = user.courses.all()
        user_skills = user.user_skills.filter(editable=False)
        courses = Course.objects.all()
        obj = []
        for course in courses:
            for skill in user_skills:
                if skill in course.skills.all():
                    if course not in user_courses:
                        obj.append(course)
                        break
        serializer = CourseSerializer(obj, many=True)
        return Response(serializer.data)


class RecommendedCoursesCollectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Возвращает рекомендованные курсы по максимальному количеству
        совпадений навыков пользователя и навыков подборки."""

        # Это очень плохой алгоритм((
        user = get_object_or_404(CustomUser, id=self.request.user.id)
        user_courses = user.courses.all()
        selection = get_object_or_404(Selection, pk=self.kwargs.get("pk"))
        selection_skills = selection.skills.all()
        user_skills = user.user_skills.filter(editable=False)
        user_skills_in_selection = []
        skills_counters = []
        courses_for_recommend = []
        obj = []

        # Проверяем какие курсы совпадают с подборкой
        for skill in user_skills:
            if skill in selection_skills:
                user_skills_in_selection.append(skill)
        courses = Course.objects.all()

        # Удаляем курсы из списка которые пользователь уже прошел
        for course in courses:
            if course not in user_courses:
                courses_for_recommend.append(course)

        # Получаем список с количеством вхождений навыков пользователя в
        # навыки курса
        for course in courses_for_recommend:
            counter = 0
            for user_skill in user_skills_in_selection:
                for course_skill in course.skills.all():
                    if user_skill == course_skill:
                        counter += 1
                        if counter == len(user_skills_in_selection):
                            break
            skills_counters.append(counter)

        # Получаем индексы чтобы взять по ним курсы для рекомендаций
        for index in range(len(skills_counters)):
            if skills_counters[index] != 0:
                obj.append(courses_for_recommend[index])

        # Если по максимальному количеству
        # совпадений навыков пользователя и навыков подборки
        # ничего не порекомендовать, то рекомендация только на
        # основании скиллов в подборке по хотя бы одному совпадению
        if len(obj) == 0:
            for course in courses_for_recommend:
                for skill in selection_skills:
                    if skill in course.skills.all():
                        obj.append(course)
                        break

        serializer = CourseSerializer(obj, many=True)
        return Response(serializer.data)


class RecommendedCoursesSkillView(APIView):
    permission_classes = [IsAuthenticated]

        def get(self, request, pk):
        """Возвращает рекомендованные курсы на основе открытого наыка."""
        skill = get_object_or_404(Skill, id=pk)
        user_courses = request.user.courses.all()

        courses = Course.objects.prefetch_related('skills').exclude(id__in=user_courses.values_list('id', flat=True))
        courses_for_recommend = courses.filter(skills=skill)

        if courses_for_recommend.exists():
            serializer = CourseSerializer(random.choice(courses_for_recommend))
            return Response(serializer.data)
        return Response({})
        # skill = get_object_or_404(Skill, id=pk)
        # user_courses = request.user.courses.all()
        # courses = Course.objects.all()
        # user_courses = request.user.courses.all()
        # courses_for_recommend = []
        # obj = []
        # for course in courses:
        #     if course not in user_courses:
        #         courses_for_recommend.append(course)
        # for course in courses_for_recommend:
        #     if skill in course.skills.all():
        #         obj.append(course)
        # if len(obj) != 0:
        #     serializer = CourseSerializer(random.choice(obj))
        #     return Response(serializer.data)
        # return Response({})


class SkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        skills = Skill.objects.filter(editable=False)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Пытаемся понять есть ли у нас такой скилл в базовых,
        # если нет то сохраняем is_custom_skill True
        # потому что понимаем что скилл пользователь придумал сам

        is_custom_skill = True
        not_editable_skills = Skill.objects.filter(editable=False)
        for skill in not_editable_skills:
            if request.data.get("name") == skill.name:
                is_custom_skill = False
                break

        # Если скилл кастомный то нужно добавить его в общую таблицу
        # и пометить editable True
        if is_custom_skill:
            # Конструкция позволяет пользователям думать что они создали
            # свой навык и добавили его себе, на самом деле при совпадении
            # по имени из БД возьмется существующий навык
            # чтобы избежать дублирования одного и того же кастомного
            # навыка разными пользователями
            skill, editable = Skill.objects.get_or_create(
                name=request.data.get("name"), editable=True
            )

        # Связываем навык и пользователя после добавления в базу
        # либо из тех что в базе есть
        user_skill = {
            "editable": is_custom_skill,
            "rate": 0,
            "notes": "",
        }
        serializer = UserSkillSerializer(data=user_skill)
        if serializer.is_valid():
            try:
                serializer.save(skill=skill, user=self.request.user)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            except Exception:
                return Response({"Этот навык уже имеется!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteSkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        user_skill = get_object_or_404(UserSkill, id=pk)
        if request.data.get("name") is not None:
            name = request.data.pop("name")
            skill = get_object_or_404(Skill, id=pk)
            if skill.editable is True:
                skill.name = name
                skill.save()
        serializer = PatchUserSkillSerializer(
            user_skill, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
        user_skill = {
            "id": user_skill.id,
            "name": get_object_or_404(Skill, id=user_skill.skill_id).name,
            "rate": user_skill.rate,
            "notes": user_skill.notes,
            "editable": user_skill.editable,
        }
        return Response(user_skill)

    def delete(self, request, pk):
        user_skill = get_object_or_404(UserSkill, id=pk)
        user_skill.delete()
        data = {
            "id": pk,
            "name": get_object_or_404(Skill, id=user_skill.skill_id).name,
            "rate": user_skill.rate,
            "notes": user_skill.notes,
            "editable": user_skill.editable,
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class UserDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_skills = UserSkill.objects.filter(user=request.user)
        print(user_skills)
        serializer = UserDataSkillSerializer(user_skills, many=True)
        return Response(serializer.data)


class UserDataViewSet(ListViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDataSkillSerializer

    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user)


class CollectionsViewSet(ListViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SelectionSerializer
    queryset = Selection.objects.all()
