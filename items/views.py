from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Items


def index(request):
    item=Items.objects.all()
    return render(request,"index.html",{"item":item})

def cart(request):
    return render(request,"cart.html")