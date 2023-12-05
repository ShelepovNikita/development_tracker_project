from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# from skills.models import UserSkill
from courses.models import Course
from api.v1.serializers import CourseSerializer
from selections.models import Selection

from users.models import CustomUser


class RecommendedCoursesTracker(APIView):
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


class RecommendedCoursesCollection(APIView):
    def get(self, request, pk):
        """Возвращает рекомендованные курсы по максимальному количеству
        совпадений навыков пользователя и навыков подборки."""
        user = get_object_or_404(CustomUser, id=self.request.user.id)
        selection = get_object_or_404(Selection, pk=self.kwargs.get("pk"))
        selection_skills = selection.skills.all()
        user_skills = user.user_skills.filter(editable=False)
        obj = []
        ans = []
        for skill in user_skills:
            if skill in selection_skills:
                obj.append(skill)
        courses = Course.objects.all()
        for course in courses:
            counter = 0
            for skill in course.skills.all():
                if skill in obj:
                    counter += 1
                    if counter == len(obj):
                        ans.append(course)
                        break
        print(ans)

        return Response("done")


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status, viewsets
# from courses.models import Course
# from skills.models import DefaultSkill
# from api.v1.serializers import CourseSerializer
# from api.v1.serializers import DefaultSkillSerializer, UserSerializer


# class APICourses(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)


# class SkillViewSet(viewsets.ModelViewSet):
#     queryset = DefaultSkill.objects.all()
#     serializer_class = DefaultSkillSerializer


# class SelectionViewSet(APIView):
#     def get(self, request, *args, **kwargs):
#         pass


# class UserViewSet(viewsets.ModelViewSet):
#     pass


# class UserDataView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             "user": str(request.user),
#             "auth": str(request.auth),
#         }
#         return Response(content)
