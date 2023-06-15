from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import BaseUser
from accounts.permissions import NotAuthenticated, IsSuperuser, IsAuthenticated
from accounts.serializers import RegisterClientSerializer, AddPublisherSerializer, BaseUserSerializer, \
    AddContentManagerSerializer


class RegisterClientView(CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = RegisterClientSerializer
    permission_classes = (NotAuthenticated,)


class AbstractAddActorView(CreateAPIView):
    queryset = BaseUser.objects.all()
    permission_classes = (IsSuperuser,)


class AddPublisherView(AbstractAddActorView):
    serializer_class = AddPublisherSerializer


class AddContentManagerView(AbstractAddActorView):
    serializer_class = AddContentManagerSerializer


class GetUserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = BaseUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
