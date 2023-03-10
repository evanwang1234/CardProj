from django.urls import path, include
from .views import GenericUserAPIView,UserAPIView, CustomRegisterView

urlpatterns = [
   path('users/', UserAPIView.as_view()),
   path('user/<int:id>', GenericUserAPIView.as_view()),
   path('register/', CustomRegisterView.as_view()),
   path('', include('allauth.account.urls')),
   #path('', include('rest_auth.registration.urls')),
   path('', include('rest_framework.urls'))
]