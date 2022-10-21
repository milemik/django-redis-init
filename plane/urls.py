from django.urls import path

from plane.views import UserRedisView

app_name = "plane"

urlpatterns = [
    path("", UserRedisView.as_view(), name="all_planes")
]
