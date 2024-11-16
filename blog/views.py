from django.shortcuts import render, get_object_or_404
from .models import Character
from .models import Equipement

# Create your views here.


def post_list(request):
    personnes = Character.objects.all()
    #personne = get_object_or_404(Character, pk=pk)
    return render(request, 'blog/post_list.html', {'personnes': personnes})