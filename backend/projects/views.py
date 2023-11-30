from .modelFile.Users import Users
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .serializerFile.Users import UsersSerializer

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        request.data["password"] = make_password(request.data["password"])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():    
            user = serializer.save()
            usersAppSerializer = UsersSerializer(data={
                "username": request.data["username"],
                "email": request.data["email"],
                "password": request.data["password"],
            })
            if usersAppSerializer.is_valid():
                usersAppSerializer.save()
                # Genera un token para el nuevo usuario
                token, created = Token.objects.get_or_create(user=user)

                # Devuelve el token junto con los datos del usuario
                response_data = {
                    'token': token.key,
                    'userDjango': serializer.data,
                    'userApp': usersAppSerializer.data,
                }
            
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(usersAppSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        request.data["password"] = make_password(request.data["password"])
        user = Users.objects.filter(email=request.data["email"])
        # Genera un token para el nuevo usuario
        #token, created = Token.objects.get_or_create(user=user)

        # Devuelve el token junto con los datos del usuario
        response_data = {
            #'token': token.key,
            'userApp': user,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
