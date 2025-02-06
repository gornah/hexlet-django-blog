# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm

# def index(request):
#  return render(request, 'articles/index.html', context={
#         'app_name': 'hexlet_django_blog.article'
#     })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        # context = {'app_name': 'hexlet_django_blog.article'}
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно создана!')
            return redirect('articles_index')
        messages.error(request, 'Ошибка в заполнении формы!')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id,
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно обновлена!')
            return redirect('articles_index')

        messages.error(request, 'Ошибка в заполнении формы!')
        return render(request, 'articles/update.html', context={
            'form': form,
            'article_id': article_id,
        })
