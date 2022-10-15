from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random
from .models import Invitation
from .utilities import send_invitation, invitation_accepted
# Create your views here.
def invite(request):
   # breakpoint()
    user = get_object_or_404(User, pk=request.user.id)
    #breakpoint()
    if request.method=='POST':
        email = request.POST.get('email')
        
        if email:
            #breakpoint()
            invitations = Invitation.objects.filter(user=user.id, email=email)
            if not invitations:
                
                code = ''.join(random.choice('sdasdadndj3442nnnds324') for i in range(4))
                invitation = Invitation.objects.create(user=user, email=email, code=code)
                
                messages.info(request, 'The user was invited')
                send_invitation(email, code, user.username)
            else:
                messages.info(request, 'The user has been already invited')
    
     
    return render(request, 'invite.html',{'user':user})

def accept_invitation(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        invitations = Invitation.objects.filter(code=code, email=request.user.email)
        if invitations:
            invitation = invitations[0]
            invitation.status = Invitation.ACCEPTED
            invitation.save()
            
        #     user = invitation.user
        #    # user.add(request.user)
        #     user.save()
            
            messages.info(request, 'Invitation accepted')
            
            invitation_accepted(request.user, invitation)
            
            #return redirect('')
        else:
            messages.info(request, 'Invitation was not found')
    else:
        return render(request, 'invitation_accepted.html')
    

def invite_index(request):
    return render(request, 'invite_home.html')