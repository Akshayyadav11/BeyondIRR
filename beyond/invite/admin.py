# Register your models here.
from django.contrib import admin
from .models import Invitation
# Register your models here.

class InviteAdmin(admin.ModelAdmin):
    list_display = ('user', 'email','code' ,'status','date_sent')
    list_filter = ("status",)
    search_fields = ['email', 'status']
    #prepopulated_fields = {'slug': ('title',)}
    
   

admin.site.register(Invitation, InviteAdmin)