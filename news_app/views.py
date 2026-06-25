from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import News
from .forms import NewsForm, CustomUserCreationForm, UserUpdateForm

def home_view(request):
    news_list = News.objects.all().order_by('-date_created')
    return render(request, 'home.html', {'news_list': news_list})

def news_detail_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news_detail.html', {'news': news})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна! Добро пожаловать!')
            return redirect('news_app:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')
                return redirect('news_app:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён!')
            return redirect('news_app:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Аккаунт удалён.')
        return redirect('news_app:home')
    return render(request, 'profile_confirm_delete.html')

@login_required
def news_create_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, 'Новость добавлена!')
            return redirect('news_app:news_detail', news_id=news.id)
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form, 'title': 'Добавить новость'})

@login_required
def news_edit_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать эту новость")
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новость обновлена!')
            return redirect('news_app:news_detail', news_id=news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form': form, 'title': 'Редактировать новость', 'news': news})

@login_required
def news_delete_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить эту новость")
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Новость удалена!')
        return redirect('news_app:home')
    return render(request, 'news_confirm_delete.html', {'news': news})