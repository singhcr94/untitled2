from django.urls import path,include
from App import views
from rest_framework import routers
urlpatterns = [
    path('',views.personview),
    path('<int:pk>',views.detail)]
