from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.AuthUserRegisterView.as_view(), name='register'),
    path('signin/', views.AuthUserSignInView.as_view(), name='signin'),
    path('recovery/', views.AuthUserRecoveryView.as_view(), name='recovery'),
    path('otp/', views.AuthUserOtpView.as_view(), name='otp'),
    path('reset-password/<uuid:uuid>/<str:token>/', views.AuthUserResetPasswordView.as_view(), name='reset-password'),
]
