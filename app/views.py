from datetime import datetime
from .models import Blog, Comment
from .forms import CommentForm
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .forms import BlogForm




def home(request):
    return render(
        request,
        'app/index.html',
        {
            'title': 'Главная страница',
            'year': datetime.now().year,
        }
    )

def about(request):
    return render(
        request,
        'app/about.html',
        {
            'title': 'О проекте',
            'message': 'Этот сайт посвящён АвтоВАЗ — крупнейшему автопроизводителю России и бренду LADA.',
            'year': datetime.now().year,
        }
    )

def links(request):
    return render(
        request,
        'app/links.html',
        {
            'title': 'Полезные ресурсы',
            'year': datetime.now().year,
        }
    )

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'app/thank_you.html', {'data': data})
    else:
        form = FeedbackForm()

    return render(request, 'app/pool.html', {'form': form})

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('home')
    else:
        regform = UserCreationForm()

    return render(request, 'app/registration.html', {
        'regform': regform,
        'year': datetime.now().year,
    })








def blog(request):
    """Страница со списком статей"""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()
    return render(request, 'app/blog.html', {
        'title': 'Блог',
        'posts': posts,
        'year': datetime.now().year
    })

def blogpost(request, parametr):
    """Страница отдельной статьи с комментариями"""
    post_1 = get_object_or_404(Blog, id=parametr)
    comments = Comment.objects.filter(post=post_1).order_by('-date')  # комментарии к статье

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = post_1
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(request, 'app/blogpost.html', {
        'post_1': post_1,
        'comments': comments,
        'form': form,
        'year': datetime.now().year,
    })



def newpost(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.posted = datetime.now()
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'app/newpost.html', {
        'form': form,
        'title': 'Добавить статью',
        'year': datetime.now().year
    })

def videopost(request):
    return render(request, 'app/videopost.html')