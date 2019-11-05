from django.shortcuts import render,get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

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

def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('home')  #Here home = name of url
    return render(request, 'article_form.html', {'form': form})

def update_article(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
       form.save()
       return redirect('home')  #Here home = name of url
    return render(request, 'article_form.html', {'form': form, 'article': article})

def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
       article.delete()
       return redirect('home')  #Here home = name of url
    return render(request, 'article_del_conf.html', {'article': article})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})