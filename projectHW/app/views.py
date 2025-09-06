from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def user_list(request) :
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users' : users})

def user_detail(request, pk) :
    user = get_object_or_404(User, pk= pk)
    return render(request, 'users/user_detail.html', {'users' : user})

