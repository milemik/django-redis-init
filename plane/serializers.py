from rest_framework import serializers


class UserRedisSerializer(serializers.Serializer):
    model_key = serializers.CharField(allow_null=False, allow_blank=False)
    plane_name = serializers.CharField(allow_null=False, allow_blank=False)
    plane_active = serializers.BooleanField(default=False, allow_null=False)
