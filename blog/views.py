from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_view(request):
    if request.method == "GET":
        return HttpResponse("This is the GET blog page")
    elif request.method == "POST":
        return HttpResponse("This is a POST to the Blog")