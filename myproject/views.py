from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def index(request):

    return render(request, 'index.html')