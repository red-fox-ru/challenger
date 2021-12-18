from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from v1.serializers.auth import UserSerializer, GetPairTokenSerializer, UserSerializerWithToken


class GetTokenView(TokenObtainPairView):
    serializer_class = GetPairTokenSerializer


@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_id(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    if request.method == 'PUT':
        serializer = UserSerializerWithToken(user, many=False)
        data = request.data
        user.username = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        if data['password'] != '':
            user.password = make_password(data['password'])
        user.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    user_for_delete = User.objects.get(id=pk)
    user_for_delete.delete()
    return Response('User was deleted')
