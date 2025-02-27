from django.urls import path

# from hexlet_django_blog.article import views
# from .views import ArticleIndexView
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView
)


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>', ArticleView.as_view(), name='article_detail'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    # path('<inr:article_id>/comment/<int:id>', ArticleCommentsView.as_view()),
]
