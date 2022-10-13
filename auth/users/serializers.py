from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User        
        fields = ['name', 'email', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def create(self, validated_data):       
        return User.objects.create_user(**validated_data)
        

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("passwords not match")
        return attrs 
    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User        
        fields = ['email', 'password']
        extra_kwargs={
            'password':{'write_only':True}
        }
     