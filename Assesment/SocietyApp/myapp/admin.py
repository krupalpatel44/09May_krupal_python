from django.contrib import admin
from .models import *

# Register your models here.



class userregister(admin.ModelAdmin):
    ordering=['id']
    list_display=['firstname','lastname','gender','mobile']

class watchmanadmin(admin.ModelAdmin):
    ordering=['id']
    list_display=['firstname','lastname','gender','mobile']

class notice(admin.ModelAdmin):
    ordering=['id']
    list_display=['member_name','mobile','email']

class event(admin.ModelAdmin):
    ordering=['id']
    list_display=['event_title','start_date','end_date']

admin.site.register(registerdata,userregister)
admin.site.register(watchman,watchmanadmin)
admin.site.register(noticedata,notice)
admin.site.register(eventdata,event)