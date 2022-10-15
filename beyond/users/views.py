
import email
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from datetime import datetime
import datetime
from rest_framework.authentication import authenticate
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth import login
from django.views import View
import jwt
from rest_framework.exceptions import AuthenticationFailed
from .forms import NewUserForm
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from invite.models import Invitation
from invite.views import accept_invitation
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                breakpoint()
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                
                invitations = Invitation.objects.filter(email=user.email, status=Invitation.INVITED)
                breakpoint()
                if invitations:
                    breakpoint()
                    accept_invitation(request)
                    #return redirect('invite:accept_invitation')
                
                return redirect('users:login')
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('blog:blog_list')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


@login_required(redirect_field_name='login', login_url='/login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('users:login')


def user_index(request):
    return render(request,'base.html')