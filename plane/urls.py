from django.urls import path

from plane.views import PlaneRedisView

app_name = "plane"

urlpatterns = [
    path("", PlaneRedisView.as_view(), name="all_planes"),
]
