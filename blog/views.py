from django.shortcuts import render
from django.views import generic
from .models import Post
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

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6