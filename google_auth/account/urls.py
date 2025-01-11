# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),

    
]