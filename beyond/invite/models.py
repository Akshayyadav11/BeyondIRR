from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Invitation(models.Model):
    
    INVITED = 'invited'
    ACCEPTED = 'accepted'
    
    CHOICE_STATUS = (
        (INVITED , 'invited'),
        (ACCEPTED , 'accepted')
    )
    
    user = models.ForeignKey(User, related_name = 'invitations' , on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=CHOICE_STATUS, default=INVITED)
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email