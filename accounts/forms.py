from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ("email", "username",)
    

class CustomUserChangeForm(UserChangeForm):

    class Meta:
      model = User
      fields = ("email", "username",)


from django.contrib.auth.forms import AuthenticationForm

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass