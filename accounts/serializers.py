from .models import User
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.utils import (email_address_exists,
                               get_username_max_length)
from allauth.account.utils import setup_user_email


class CustomUserDetailsSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fieds = ('email')
    read_only_fields = ('email',)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password' ]
    write_only_fields = ('password',)
  def create(self, validated_data):
    user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
        )
    user.set_password(validated_data['password'])
    
    user.save()
    return user

  def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.set_password(validated_data.get('password', instance.password))
    instance.username = validated_data.get('username', instance.username)
    instance.save()
    return instance


class CustomRegisterSerializer(RegisterSerializer):
  pass
"""  email = serializers.EmailField(required = True)
  username = serializers.CharField(required = True)
  password = serializers.CharField(write_only = True)
  
    
  def validate_email(self, email):
    #email = get_adapter().clean_email(email)
    #if email and email_address_exists(email):
    try:
      if User.objects.get(email = email):
        raise serializers.ValidationError(("A user is already registered with this e-mail address."))
    except User.DoesNotExist:
      return email

  def validate_username(self, username):
    try:
      if User.objects.get(username = username):
        raise serializers.ValidationError(("A user is already registered with this username."))
    except User.DoesNotExist:
      return username
  

  def validate_password(self, password):
    #return get_adapter().clean_password(password)
    return password
      
  def get_cleaned_data(self):

    return {
      'password': self.validated_data.get('password',''),
      'email': self.validated_data.get('email', ''),
      'username': self.validate_data.get('username', ''),
    }
  def custom_signup(self, request, user):
      pass
  
  def save(self, request):
    pass

    adapter = get_adapter()
    user = adapter.new_user(request)
    self.cleaned_data = self.get_cleaned_data()
    adapter.save_user(request, user, self)
    self.custom_signup(request, user)
    setup_user_email(request, user, [])
    return user
  """