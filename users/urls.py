from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChangePasswordView, ResetPasswordView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset-password'),
]