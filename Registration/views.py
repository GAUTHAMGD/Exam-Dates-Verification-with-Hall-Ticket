# django imports
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from django.utils.crypto import get_random_string

# external imports
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.viewsets import ViewSet

# local imports
from .models import AuthToken, User
from .serializers import AuthUserSerializer


class AuthUserViewSet(ViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()

    def register(self, request):
        data = request.data
        if data.get("password"):
            data["password"] = make_password(data["password"])

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

        instance = serializer.save()
        data = self.serializer_class(instance=instance).data
        return Response(data=data, status=HTTP_201_CREATED)

    def login(self, request):
        data = request.data
        if not data.get("username"):
            return Response(data={"username": "Required field."}, status=HTTP_400_BAD_REQUEST)
        if not data.get("password"):
            return Response(data={"password": "Required field."}, status=HTTP_400_BAD_REQUEST)

        blog_user = User.objects.get(username=data.get("username"))
        if not check_password(data.get("password"), blog_user.password):
            return Response(data={"password": "Invalid password."}, status=HTTP_400_BAD_REQUEST)

        auth_token = AuthToken.objects.filter(user=blog_user).last()
        if auth_token:
            auth_token.delete()
        token = get_random_string(length=100)
        AuthToken.objects.create(token=token, user=blog_user, created_at=timezone.now())

        data = self.serializer_class(instance=blog_user).data
        data.update({"token": token})
        return Response(data=data, status=HTTP_200_OK)

    def logout(self, request):
        authorization = request.META.get("HTTP_AUTHORIZATION")
        if not authorization:
            return Response(data={"authorization": "Required Authorization."}, status=HTTP_401_UNAUTHORIZED)
        auth_token = AuthToken.objects.filter(token=authorization)
        if not auth_token.exists():
            return Response(data={"authorization": "Invalid Authorization."}, status=HTTP_401_UNAUTHORIZED)
        auth_token = auth_token.last()
        username = auth_token.user.username
        auth_token.delete()
        return Response(data={"logout": f"{username} has logged out successfully"}, status=HTTP_200_OK)

