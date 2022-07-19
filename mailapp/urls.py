from django.contrib import admin
from django.urls import path,include
from mailapp import views
urlpatterns = [
    path('',views.greetings),
    path('send',views.send)
]