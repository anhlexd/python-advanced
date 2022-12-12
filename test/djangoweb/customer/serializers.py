from rest_framework import serializers
from customer.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ["id", "first_name", "email","last_name","password", "username"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True, required=True, validators= [validate_password]
    )

    class Meta:
        model = User
        fields = ('username', 'password','email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name' : {'required': True}
        }

        
    def create(self, validated_data):
        try:
        
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
            )

            return user
      
        except:
            raise serializers.ValidationError("Register unsuccessful")
        
    
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        
    def login_request(self, request):
        uname = request.data('uname')
        pwd = request.data('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




