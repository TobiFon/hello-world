from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(request):
  return HttpResponse('hello world')

# Create your views here.
