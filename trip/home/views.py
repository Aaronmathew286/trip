from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

def index(request):
    return render(request,"index.html")

def test(request):
    val="java"
    return render(request,"test.html",{'a':val})
