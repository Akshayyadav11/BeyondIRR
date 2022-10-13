
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from datetime import datetime
import datetime
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.authentication import authenticate
from .models import User
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from django.contrib.auth import login
from django.views import View
import jwt
from rest_framework.exceptions import AuthenticationFailed
from .forms import RegisterForm

class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# class Register(View):
#     def get(self, request):
#         obj = RegisterForm()
#         return render(request, "signup_form.html", {'form': obj})
#         #return Response(obj)

#     def post(self, request):
#         obj = RegisterForm(request.POST)
#         if obj.is_valid():
#             obj.save()
#             return redirect('blog:')
#         else:
#             return render(request, "signup_form.html", {'form': obj})
                  

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
        # #return Response({'message':'Login successfully !!'})
        # return HttpResponse(
        #       json.dumps(token),
        #       status=200,
        #       content_type="application/json"
        #     )
        #breakpoint()
        loginserializer = UserLoginSerializer(data=request.data)
        if loginserializer.is_valid(raise_exception=True):
            
            email = loginserializer.data.get('email')
            password = loginserializer.data.get('password')
            user = authenticate(request, email=email, password=password)
            #breakpoint()
            if user is not None:
                login(request, user)
                return Response({'message':'Login successfully !!'})
            else:
                return Response({'message':'Invalid User!!'})
            



# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib import auth

# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 User.objects.get(username = request.POST['username'])
#                 return render (request,'signup.html', {'error':'Username is already taken!'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
#                 auth.login(request,user)
#                 return redirect('users:login')
#         else:
#             return render (request,'signup.html', {'error':'Password does not match!'})
#     else:
#         return render(request,'signup.html')

# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect('users:login')
#         else:
#             return render (request,'login.html', {'error':'Username or password is incorrect!'})
#     else:
#         return render(request,'login.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return redirect('users:login')

