from django.shortcuts import render, get_object_or_404
from .models import Character
from .models import Equipement

# Create your views here.


def post_list(request):
    personnes = Character.objects.all()
    #personnes = get_object_or_404(Character, pk=pk)
    return render(request, 'blog/post_list.html', {'personnes': personnes})


def post_detail(request, pk):
    personne = get_object_or_404(Character, pk=pk)
    return render(request, 'blog/post_detail.html', {'personne': personne})