from django.shortcuts import render


# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter().order_by('published_time').all()
    return render(request, 'blog/post_list.html', {'posts': posts})
