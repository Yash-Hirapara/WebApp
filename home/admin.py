from django.contrib import admin
from .models import contact,signup_master
# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','city']

class signup_masterAdmin(admin.ModelAdmin):
	list_display=['firstname','lastname','email_id','contact_no']

admin.site.register(contact,contactAdmin)

admin.site.register(signup_master,signup_masterAdmin)