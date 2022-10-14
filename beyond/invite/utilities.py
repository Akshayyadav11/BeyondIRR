from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_invitation(to_email, code, user):
    from_email = settings.EMAIL_HOST_USER
    accept_url = settings.ACCEPTATION_URL
    
    subject = 'Invitation to Blog'
    text_content = 'Invitation to Blog, Your code is : %s' % code
    html_content = render_to_string('email_invitation.html', {'code':code, 'user':user, 'accept_url':accept_url})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    

def invitation_accepted(user, invitation, to_email):
    from_email = settings.EMAIL_HOST_USER
    
    
    subject = 'Invitation accepted'
    text_content = 'Your Invitation was accepted'
    html_content = render_to_string('invitation_accepted.html', {'user':user, 'invitation':invitation})
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()