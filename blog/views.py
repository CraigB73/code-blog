from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse
# Create your views here.

# def post_view(request):
#     if request.method == "GET":
#         return HttpResponse("This is the GET blog page")
#     elif request.method == "POST":
#         return HttpResponse("This is a POST to the Blog")

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = "post_list.html"