from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def articles(request):
    # get articles
    articles = Article.objects.all()
    #pages articles
    paginator = Paginator(articles, 2)

    # Get number page
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)



    return render(request,'articles/list.html',{
        'title': 'Articles',
        'articles': page_articles
    })
@login_required(login_url='login')
def article_detail(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    
    
    return render(request, 'articles/detail.html', {
        'article': article
    })

@login_required(login_url='login')
def categories(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category)


    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles
    })
