from django.shortcuts import render, get_object_or_404
from .models import Character
from .models import Equipement
from .forms import MoveForm

# Create your views here.


def post_list(request):
    personnes = Character.objects.all()
    #personnes = get_object_or_404(Character, pk=pk)
    return render(request, 'blog/post_list.html', {'personnes': personnes})


def post_detail(request, pk):
    personne = get_object_or_404(Character, pk=pk)
    return render(request, 'blog/post_detail.html', {'personne': personne})

# Create your views here.
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'blog/character_list.html', {'characters': characters})
 
def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    lieu = character.lieu
    form=MoveForm()
    return render(request,
                  'blog/character_detail.html',
                  {'character': character, 'lieu': lieu, 'form': form})