from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1.views import (
    CollectionsViewSet,
    RecommendedCoursesTrackerView,
    RecommendedCoursesCollectionView,
    RecommendedCoursesSkillView,
    SkillsView,
    UpdateDeleteSkillsView,
    UserDataViewSet,
)


router_v1 = SimpleRouter()
router_v1.register("userData", UserDataViewSet, basename="user_data")
router_v1.register("collections", CollectionsViewSet, basename="user_data")
urlpatterns = [
    path("", include(router_v1.urls)),
    path(
        "recommended-courses-tracker/",
        RecommendedCoursesTrackerView.as_view(),
        name="recommended_courses_tracker",
    ),
    path(
        "recommended-courses-collection/<int:pk>/",
        RecommendedCoursesCollectionView.as_view(),
        name="recommended_courses_collection",
    ),
    path(
        "recommended-courses-skill/<int:pk>/",
        RecommendedCoursesSkillView.as_view(),
        name="recommended_courses_collection",
    ),
    path(
        "skills/",
        SkillsView.as_view(),
        name="skills",
    ),
    path(
        "skills/<int:pk>/",
        UpdateDeleteSkillsView.as_view(),
        name="skills",
    ),
]
