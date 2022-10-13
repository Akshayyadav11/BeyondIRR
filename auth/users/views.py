
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework.authentication import authenticate


from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from django.views import View


class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
            

class Login(APIView):
    def post(self, request):
        # email = request.data['email']
        # password = request.data['password']
        # user = User.objects.filter(email=email).first()
        # if user is None:
        #     raise AuthenticationFailed('User not found')
        
        # if not user.check_password(password):
        #     raise AuthenticationFailed('Incorrect password')
        
        # payload ={
        #     'id':user.id,
        #     'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=60),
        #     'iat':datetime.datetime.utcnow()
        # }
        
        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        # return Response({'message':'Login successfully !!'})
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'message':'Login successfully !!'})
            else:
                return Response({'message':'Invalid user successfully !!'})
            
