from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name="list_articles"),
    path('category/<int:category_id>', views.categories, name="categories"),
    path('articles/<int:article_id>', views.article_detail, name="detail")
]