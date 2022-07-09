from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from user.models import User
from user.api.serializer import UserRegisterSerializer, UserSerializer, UserUpdateSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
      user = User.objects.get(id=request.user.id)
      serializer = UserUpdateSerializer(user, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)