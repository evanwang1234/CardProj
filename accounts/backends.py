from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from .models import User
class MyBackend(BaseBackend):
  def authenticate(self, request, email = None, username = None, password= None):
    print("lolsodkdssd")
    try:
      print("loolllloo")
      print(email)
      print(username)
      print(password)
      user = User.objects.get(email=username)
      if user.check_password(password):
        print("WORKED")
        return user
    except User.DoesNotExist:
      return None
    
  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None

    