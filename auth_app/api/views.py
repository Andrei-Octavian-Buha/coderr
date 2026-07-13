from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, CustomTokeObtainPairSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokeObtainPairSerializer
    def post(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = Response({"message":"Login erfolgreich"})
        refresh = response.data.get("refresh")
        access = response.data.get("access")

        response.set_cookie(
            key= "access_token",
            value=access,
            httponly=True,
            secure=True,
            samesite="Lax"
        )
        response.set_cookie(
            key= "refresh_token",
            value=refresh,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        response.data = {"msg":"Succesed login"}

        return response

class CookieTokenRefreshView(TokenRefreshView):
    def post(self,request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            return Response (
                {"detail":"Refresh token not found!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data={"refresh":refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response (
                {"detail":"Refresh token not found!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        
        access_token = serializer.validated_data.get("access")
        response = Response({"message":"acces Token refreshed"})
        response.set_cookie(
            key= "access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Lax"
        )

        return response

class RegisterView(APIView):
    """
    Handles user registration.
    
    Accepts user credentials, creates a new user account, and returns 
    an authentication token along with basic user information.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token , _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "email": user.email,
                    "user_id": user.id,
                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(ObtainAuthToken):
    """
    Handles user authentication.
    
    Verifies provided credentials and returns an authentication token 
    if the login is successful, allowing access to protected endpoints.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            data = {
                "token": token.key,
                "username":user.username,
                "email": user.email,
                "user_id":user.id
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
