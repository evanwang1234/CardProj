from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer, CustomUserDetailsSerializer, CustomRegisterSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate

class CustomRegisterView(RegisterView):
  queryset = User.objects.all()
  serializer_class = CustomRegisterSerializer
  #permission_classes = (permissions.IsAdminUser,)
  authentication_classes = (authentication.SessionAuthentication,)
"""  def post(self, request, format='json'):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      if user:
        token, _ = Token.objects.get_or_create(user=user)
        json = serializer.data
        json['token'] = token.key
        response = Response(json, status=status.HTTP_201_CREATED)
        response['Authorization'] = 'Token ' + token.key
        #login(response)
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     response = JsonResponse(json, status=status.HTTP_201_CREATED)
        response['token'] = token.key
        response['Authorization'] = 'Token ' + token.key
        return response
"""
    
    
class UserAPIView(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  #permission_classes = (IsAuthenticated,)
  def get(self, request):
    users = User.objects.all()
    print(users)
    serializer = UserSerializer(users, many = True)
    print(serializer.data)
    return Response(serializer.data)

  def get_queryset(self):
    user = self.request.user
    return user.accounts.all()

class GenericUserAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  serializer_class = UserSerializer
  queryset = User.objects.all()

  lookup_field = 'id'

  def get(self, request, id =None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)
    #user = User.objects.get(id=request.user.id)
    #serializer = UserSerializer(user)
    #return Response(serializer.data)
  def post(self, request):
    return self.create(request)

  def put(self, request, id = None):
    return self.update(request, id)

  def delete(self, request, id):
    return self.destroy(request, id)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

