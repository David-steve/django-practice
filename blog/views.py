import json

import requests
import yaml
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post
from mixed.utils import get_current_date, date_format


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


def golden_point(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])

        collect = []
        base_points = [0, 0.168, 0.382, 0.5, 0.618, 0.736, 1]

        if num1 < num2:
            # base_points = [-i for i in base_points]
            pass
        else:
            base_points.extend([1.168, 1.382, 1.5, 1.618, 1.736, 2])

        top = max(num1, num2)
        bottom = min(num1, num2)

        for point in base_points:
            number = (top - bottom) * point + bottom
            collect.append(round(number, 2))

        result = json.dumps(dict(zip(base_points, collect)), indent=4)

        return HttpResponse(result)
        pass
    else:
        return render(request, 'blog/golden_point.html')


def get_free_nodes_url(node_type):
    types = {'v2ray': '.txt', 'clash': '.yaml'}

    today = get_current_date()
    year_month = date_format(today, output_format='%Y/%m')
    today_after = date_format(today, output_format='%Y%m%d')

    node_type = types.get(node_type)

    url = f"https://www.freeclashnode.com/uploads/{year_month}/4-{today_after}{node_type}"
    return url


def v2ray_nodes(request):
    url = get_free_nodes_url('v2ray')

    # 重定向
    return redirect(url)


def clash_nodes(request):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML}, like Gecko)"
    }
    url = get_free_nodes_url('clash')

    response = requests.get(url, headers=headers)

    # 解析yaml
    ret = dict()
    try:
        ret = yaml.load(response.text, Loader=yaml.FullLoader)
    except Exception as e:
        print(e)

    # 去掉 'proxy-groups' 跟 'rules
    ret.pop('proxy-groups')
    ret.pop('rules')

    # 重定向
    return HttpResponse(yaml.dump(ret))
