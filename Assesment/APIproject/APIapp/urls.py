from django.contrib import admin
from django.urls import path
from APIapp import views

urlpatterns = [
    path('',views.snippet_list),
    path('snippet_create/',views.snippet_create),
    path('snippet_detail/<int:id>',views.snippet_detail),
    path('snippet_update/<int:id>',views.snippet_update),
    path('snippet_delete/<int:id>',views.snippet_delete),
    path('snippet_select_update/<int:id>',views.snippet_select_update),
]