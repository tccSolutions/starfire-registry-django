from django.shortcuts import render
from datetime import date
from .models import Post
from .forms import PostForm

def forum(request):
    posts = Post.objects.all()
    post_form = PostForm()
    context = {'posts': posts, 'post_form':post_form}

    if request.method == "POST":       
        form = PostForm(request.POST)
        if form.is_valid():
          post = form.save(commit=False)         
          post.save()         
        else:
            print("Form not Valid")
    return render(request, 'forum/forum.html', context)

def post(request, pk, title):
  post = Post.objects.get(id=pk)
  context={"post":post}
  return render(request, 'forum/post.html', context)