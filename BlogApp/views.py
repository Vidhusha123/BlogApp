from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'create_post.html')

def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('home')
    return render(request, 'edit_post.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return redirect('home')
