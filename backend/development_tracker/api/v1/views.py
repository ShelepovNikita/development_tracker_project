from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models import Course
from api.v1.serializers import CourseSerializer


class RecommendedCoursesTracker(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


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
