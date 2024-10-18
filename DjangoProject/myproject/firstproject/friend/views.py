from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.views.generic import ListView,DetailView
# Create your views here.

class FriendList(ListView):
    model = Friend
    
class FriendDetail(DetailView):
    model = Friend