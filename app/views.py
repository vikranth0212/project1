from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def JamPandu(request):
    return HttpResponse('<h1><marquee>Hi JamPandu How are you</h1></marquee>')
    