from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from .models import User
from .serializers import (
    UserSerializer
)


class RegistrationAPIView(APIView):
    serializer = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={'message': 'Registration successful'},
            status=HTTP_201_CREATED
        )


class VendorRegistrationAPIView(RegistrationAPIView):
    def post(self, request, *args, **kwargs):
        request.data['user_type'] = User.Type.VENDOR
        return super().post(request, *args, **kwargs)
