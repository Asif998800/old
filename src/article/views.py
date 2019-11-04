from django.shortcuts import render,get_object_or_404
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'home.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'detail.html', context)

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})