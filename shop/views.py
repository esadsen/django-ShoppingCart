from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")

def cart(request):
    return render(request,"cart.html")