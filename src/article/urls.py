from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_article, name='create_article'),
    path('<pk>/', views.detail, name='detail'),
    path('update/<pk>/', views.update_article, name='update_article'),
    path('delete/<pk>/', views.delete_article, name='delete_article'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]