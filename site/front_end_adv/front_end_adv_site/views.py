from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    query_set = model.objects.filter(status = 1).order_by('-created_on') # filter the post object by status equal to 1 and ordered by created date
    template_name = 'index.html'

class PostDetails(generic.DetailView):

    model = Post
    template_name = 'post_details.html'
