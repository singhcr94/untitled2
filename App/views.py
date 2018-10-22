
from django.shortcuts import render,redirect
from App import models
from rest_framework import viewsets
from .forms import create
from .models import person
from .serializers import personserializers
from django.core import serializers
from django.http import HttpResponse,JsonResponse

class personview(viewsets.ModelViewSet):
    queryset = person.objects.all()
    serializer_class = personserializers

def view(request):
    form= create(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/users')
    form=create()
    return render(request,'create.html',{'form':form})

def allusers(request):
    users=person.objects.all()
    return render(request,'users.html',{'users':users})
def profile(request,username):
    uprofile = serializers.serialize("json", {person.objects.get(firstname=username)})
    return HttpResponse(uprofile,content_type='json')
def edit(request,username):
    uprofile = person.objects.get(firstname=username)
    print(uprofile)
    form = create(instance=uprofile)
    form1 = create(request.POST, instance=uprofile)
    if request.method=="POST":
        if form1.is_valid():
            form1.save(commit=True)
            return redirect('http://127.0.0.1:8000/users')
    return render(request,'create.html',{'form':form})

def delete(request,username):
    user= person.objects.get(firstname=username)
    form=create(instance=user)
    user.delete()
    return redirect('http://127.0.0.1:8000/users')

