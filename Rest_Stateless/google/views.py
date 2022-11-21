from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.

class HelloView(APIView):
    permission_classes = (IsAuthenticated)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}
        r = request.get('https://www.googleapis.com/oauth2/v2/userinfo', params = payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']

            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()
            token = RefreshToken.for_user(user)
            response = {}
            response['username'] = user.username
            response['access_token'] = str(token.access_token)
            response['refresh_token'] = str(token)
            return Response(response)