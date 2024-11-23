from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *

# ********
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
# ********

urlpatterns = [
    path('',views.login),
    path('register/',views.register),
    path('index/',views.index,name='index'),
    path('smember/',views.smember),
    path('swatchman/',views.swatchman),
    path('notice/',views.notice),
    path('event/',views.event),
    path('profile/',views.profile),
    path('userlogout/',views.userlogout),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('resetpass/',views.resetpass,name='resetpass'),
    path('emailverify/',views.emailverify),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)