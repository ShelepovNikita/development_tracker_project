from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from courses.models import Course
from skills.models import DefaultSkill
from api.v1.serializers import CourseSerializer
from api.v1.serializers import DefaultSkillSerializer, UserSerializer


class APICourses(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = DefaultSkill.objects.all()
    serializer_class = DefaultSkillSerializer


class APISelections(APIView):
    def get(self, request, *args, **kwargs):
        pass


class UserViewSet(viewsets.ModelViewSet):
    pass


class UserDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)
