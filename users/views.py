import random
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Confirm

class ConfirmationAPIView(APIView):
    def post(self,request):
        code = request.data.get('code')
        confirm = get_object_or_404(Confirm,code=code)
        user = confirm.user
        user.is_active = True
        user.save()
        confirm.delete()
        return Response({'status':'User confirmed'})


class RegistrationAPIView(APIView):
    @staticmethod
    def post(request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**request.data)
        user.is_active = False
        user.save()
        confirm = Confirm.objects.create(user=user,code=random.randint(100000, 1000000))
        return Response({'status':'User registered','code': confirm.code},
                        status=status.HTTP_201_CREATED)




class AuthorizationAPIView(APIView):
    @staticmethod
    def post(request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key':token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)