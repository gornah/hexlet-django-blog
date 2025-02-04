# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.shortcuts import render, get_object_or_404
from hexlet_django_blog.article.models import Article

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


# class ArticleCommentsView(View):

#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article_id=kwargs['article_id'])
#         return render(request, ...)
