# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.shortcuts import render


# def index(request):
#  return render(request, 'articles/index.html', context={
#         'app_name': 'hexlet_django_blog.article'
#     })

class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'app_name': 'hexlet_django_blog.article'}
        return render(request, 'articles/index.html', context)
