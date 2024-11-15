from django.shortcuts import render
from .models import Character
from .models import Equipement

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})