from tkinter import Tk
from django.shortcuts import render,redirect
from App import models
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .forms import create
from .models import person
from .serializers import personserializers
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from celery.decorators import task
root= Tk()

@csrf_exempt
def personview(request):
    if request.method=='GET':

        queryset = person.objects.all()
        serializer = personserializers(queryset,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=personserializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
@csrf_exempt
def detail(request,pk):
    try:
        snippet=person.objects.get(pk=pk)
    except person.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=personserializers(snippet)
        return JsonResponse(serializer.data)
    elif request.method=="PUT":
        data=JSONParser().parse(snippet)
        serializer=personserializers(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method=="DELETE":
        snippet.delete()
        return HttpResponse(status=404)
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

