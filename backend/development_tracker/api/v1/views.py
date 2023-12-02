from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class CourseViewSet(APIView):
    def get(self, request, *args, **kwargs):
        data = {'hello': 'hello-world'}
        return Response(data, status=status.HTTP_200_OK)


class SkillViewSet(viewsets.ModelViewSet):
    pass


class SelectionViewSet(APIView):
    def get(self, request, *args, **kwargs):
        pass


class UserViewSet(viewsets.ModelViewSet):
    pass
