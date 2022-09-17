from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Главная страница
def index(request):    
    template = 'posts/index.html'
    return render(request, template)

# Страница с постами
def group_posts(request):
    return HttpResponse('Список постов')