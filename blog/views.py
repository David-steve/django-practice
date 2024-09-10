from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter().order_by('published_time').all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        # form 表格无效
        if not form.is_valid():
            pass

        post = form.save(commit=False)
        post.author = request.user
        post.published_time = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if not form.is_valid():
            pass

        post = form.save(commit=False)
        post.author = request.user
        post.published_time = timezone.now()
        post.save()

        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
