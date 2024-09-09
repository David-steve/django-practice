from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter().order_by('published_time').all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
