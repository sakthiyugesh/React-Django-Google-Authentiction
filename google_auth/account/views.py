# views.py

import requests
import requests_oauthlib
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer
from google_auth import settings
from django.shortcuts import redirect
from django.http import JsonResponse

class GoogleLogin(APIView):
    def post(self, request):
        token = request.data.get('token')
        response = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers={
            "Authorization": f"Bearer {token}"
        })
        user_info = response.json()

        if 'email' not in user_info:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        email = user_info['email']
        user, created = CustomUser.objects.get_or_create(email=email, defaults={
            'username': email.split('@')[0],
            'first_name': user_info.get('given_name', ''),
            'last_name': user_info.get('family_name', ''),
        })

        refresh = RefreshToken.for_user(user)
        access_token = RefreshToken.for_user(user).access_token
        access_token['user_id'] = user.id
        access_token['email'] = user.email
        access_token['first_name'] = user.first_name
        access_token['last_name'] = user.last_name
        
        return Response({
            'refresh': str(refresh),
            'access': str(access_token),
        })
    

class TwitterLogin(APIView):
    def get(self, request):
        # Step 1: Get request token
        request_token_url = 'https://api.x.com/oauth/request_token'
        oauth = requests_oauthlib.OAuth1Session(
            settings.TWITTER_API_KEY,
            client_secret=settings.TWITTER_API_SECRET,
            callback_uri=settings.TWITTER_CALLBACK_URL
        )
        fetch_response = oauth.fetch_request_token(request_token_url)                           
        request_token = fetch_response.get('oauth_token')
        request_token_secret = fetch_response.get('oauth_token_secret')

        # Step 2: Redirect user to Twitter for authorization
        authorization_url = oauth.authorization_url('https://api.x.com/oauth/authorize')
        return redirect(authorization_url)
