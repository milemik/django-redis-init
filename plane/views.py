from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from plane.redis_helper import PlanesRedis
from plane.serializers import UserRedisSerializer


class PlaneRedisView(APIView):
    def get(self, request):
        data = PlanesRedis().get_planes()
        serializer = UserRedisSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"ERROR": "bad"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        PlanesRedis().add_plane(request.data)
        return Response({"MESSAGE": "PLANE ADDED"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        PlanesRedis().edit_plane(new_data=request.data)
        return Response({"MESSAGE": "PLANE EDITED"})

    def delete(self, request):
        model_key = request.data.get("model_key")
        if model_key is None:
            raise Http404
        PlanesRedis().delete_plane(model_key=request.data.get)
        return Response({"MESSAGE": "PLANE DELETED"}, status=status.HTTP_204_NO_CONTENT)
