from django.urls import path,include
from App import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('App',views.personview)
urlpatterns = [
    path('views',include(router.urls))]
