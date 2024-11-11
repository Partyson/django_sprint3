from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import Http404


def index(request):
    current_time = timezone.now()

    # Получаем последние 5 опубликованных постов
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=current_time,
        category__is_published=True
    ).order_by('-pub_date')[:5]

    context = {
        'post_list': posts,  # Передаем посты в шаблон
    }

    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    # Получаем публикацию по ID, только если она опубликована
    post = get_object_or_404(Post, id=id, is_published=True)

    # Проверка, что категория публикации опубликована
    if not post.category.is_published:
        raise Http404("Категория публикации не опубликована")

    # Проверка, что дата публикации не позже текущего времени
    if post.pub_date > timezone.now():
        raise Http404("Публикация ещё не доступна")

    # Передаем контекст
    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    # Получаем категорию по slug
    category = get_object_or_404(Category,
                                 slug=category_slug, is_published=True)

    current_time = timezone.now()

    # Получаем все опубликованные посты в данной категории
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')

    context = {
        'category': category,  # Передаем категорию в шаблон
        'post_list': posts,  # Передаем посты в шаблон
    }

    return render(request, 'blog/category.html', context)
