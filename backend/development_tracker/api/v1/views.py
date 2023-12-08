from django.db.models import Prefetch, Count, Q
from rest_framework.views import APIView
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
    def get(self, request):
        """Возвращает рекомендованные курсы на основе хотя бы одного
        совпадения навыка пользователя с курсом, который он еще не проходил
        для страницы Трекер."""
        user = get_object_or_404(CustomUser.objects.prefetch_related('courses'), id=request.user.id)
        user_courses = user.courses.all()
        user_skills = user.user_skills.filter(editable=False).values_list('id', flat=True)

        courses_with_skills = Course.objects.prefetch_related(
            Prefetch('skills', queryset=Skill.objects.filter(id__in=user_skills))
        )
        courses = courses_with_skills.annotate(
            matching_skills_count=Count('skills', filter=Q(skills__in=user_skills))
        ).filter(matching_skills_count__gt=0).exclude(id__in=user_courses.values_list('id', flat=True))

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class RecommendedCoursesCollectionView(APIView):
    def get(self, request, pk):
        """Возвращает рекомендованные курсы по максимальному количеству
        совпадений навыков пользователя и навыков подборки."""

        user = get_object_or_404(CustomUser, id=request.user.id)
        user_courses_ids = user.courses.values_list('id', flat=True)
        selection = get_object_or_404(Selection, pk=pk)
        selection_skills_ids = selection.skills.values_list('id', flat=True)

        # Предварительно загружаем навыки для каждого курса
        courses_with_skills = Course.objects.prefetch_related(
            Prefetch('skills', queryset=Skill.objects.filter(id__in=selection_skills_ids))
        ).exclude(
            id__in=user_courses_ids
        )

        # Аннотируем количество совпадающих навыков
        courses = courses_with_skills.annotate(
            matching_skills_count=Count('skills', filter=Q(skills__id__in=selection_skills_ids))
        ).filter(
            matching_skills_count__gt=0
        ).order_by('-matching_skills_count')

        # Если нет курсов с максимальным количеством совпадений, выбираем по хотя бы одному совпадению
        if not courses:
            courses = courses_with_skills.filter(
                skills__id__in=selection_skills_ids
            ).distinct()

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class SkillsView(APIView):
    def get(self, request):
        skills = Skill.objects.filter(editable=False)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request):
        skill_name = request.data.get('name')
        is_custom_skill = not Skill.objects.filter(name=skill_name, editable=False).exists()

        skill, created = Skill.objects.get_or_create(
            name=skill_name, defaults={'editable': is_custom_skill}
        )
        user_skill_data = {
            "editable": is_custom_skill,
            "rate": 0,
            "notes": "",
        }
        serializer = UserSkillSerializer(data=user_skill_data, context={'request': request})
        if serializer.is_valid():
            serializer.save(skill=skill, user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteSkillsView(APIView):
    def patch(self, request, pk):
        user_skill = get_object_or_404(UserSkill.objects.select_related('skill'), id=pk)

        # name = request.data.pop('name', None)
        # if name is not None and user_skill.skill.editable is True:
        #     user_skill.skill.name = name
        #     user_skill.skill.save()
        serializer = PatchUserSkillSerializer(
             user_skill, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user_skill = get_object_or_404(UserSkill.objects.select_related('skill'), id=pk)
        skill_name = user_skill.skill.name

        # Удаление объекта без atomic.transaction()
        user_skill.delete()

        data = {
            "name": skill_name,
            "rate": user_skill.rate,
            "notes": user_skill.notes,
            "editable": user_skill.editable,
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class UserDataView(APIView):
    def get(self, request):
        user_skills = UserSkill.objects.filter(user=request.user)
        serializer = UserDataSkillSerializer(user_skills, many=True)
        return Response(serializer.data)


class UserDataViewSet(ListViewSet):
    serializer_class = UserDataSkillSerializer

    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user)


class CollectionsViewSet(ListViewSet):
    serializer_class = SelectionSerializer
    queryset = Selection.objects.prefetch_related('skills').all()
