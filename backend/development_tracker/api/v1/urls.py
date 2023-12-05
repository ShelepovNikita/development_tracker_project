from django.urls import include, path
from api.v1.views import RecommendedCoursesTracker

urlpatterns = [
    path(
        "recommended-courses-tracker/",
        RecommendedCoursesTracker.as_view(),
        name="courses_list",
    ),
]


# from rest_framework.routers import DefaultRouter
# from api.v1.views import (
#     APICourses,
#     SkillViewSet,
#     UserDataView,
#     # UserViewSet,
#     # SelectionViewSet,
# )
# router_v1 = DefaultRouter()
# router_v1.register(r"skills", SkillViewSet, basename="skills")
# # router.register(r"users", UserViewSet, basename="users")
# urlpatterns = [
#     path("", include(router_v1.urls)),
#     path("recommended-courses-tracker/", APICourses.as_view(), name="courses_list"),
#     path("userData/", UserDataView.as_view(), name="user"),
#     path("collections/", SelectionViewSet.as_view(), name="selections_list"),
# ]
