from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializer import UserSerializer, LoginSerialize
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail":"No active account found with the given credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        token_dict = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(token_dict, status=status.HTTP_200_OK)

class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.get_queryset().order_by('id')

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDatailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]


    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)
