from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        user_type = attrs.get('user_type')
        if user_type and user_type not in [User.Type.CUSTOMER, User.Type.VENDOR]:
            raise serializers.ValidationError({'user_type': ['Invalid user type']})
        return attrs

    def validate_password(self, value):
        validate_password(value)
        return value

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'user_type', 'password', 'onboarding_completed')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
