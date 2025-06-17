from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('verify-email/', views.verify_email),
    path('login/', views.CustomAuthToken.as_view()),
    path('upload-kyc/', views.upload_kyc),
]