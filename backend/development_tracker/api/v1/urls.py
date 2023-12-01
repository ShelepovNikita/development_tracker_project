from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, SkillViewSet, UserViewSet, SelectionViewSet

router = DefaultRouter()
router.register(r"skills", SkillViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses/', CourseViewSet.as_view(), name='courses_list'),
    path('collections/', SelectionViewSet.as_view(), name='selections_list'),
]