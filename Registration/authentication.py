# external imports
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

# local imports
from .models import AuthToken


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization = request.META.get("HTTP_AUTHORIZATION")
        if not authorization:
            raise exceptions.AuthenticationFailed("Required Authorization.")

        auth_token = AuthToken.objects.filter(token=authorization)
        if not auth_token.exists():
            raise exceptions.AuthenticationFailed("Invalid Authorization.")
        auth_token = auth_token.last()
        return (auth_token.user, auth_token)

    def authenticate_header(self, request):
        return ""
