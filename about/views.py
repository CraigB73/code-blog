from django.shortcuts import render
from .models import About
# from django.http import HttpResponse
# Create your views here.


"""
Using Function: post_view(), is bad pratice an difficult to scale
"""
# def post_view(request):
#     if request.method == "GET":
#         return HttpResponse("This is the GET blog page")
#     elif request.method == "POST":
#         return HttpResponse("This is a POST to the Blog")

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )

