from django.shortcuts import render, get_object_or_404, redirect
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
 
# def character_detail(request, id_character):
#     character = get_object_or_404(Character, id_character=id_character)
#     lieu = character.lieu
#     form=MoveForm()
#     return render(request,
#                   'blog/character_detail.html',
#                   {'character': character, 'lieu': lieu, 'form': form})

# def character_detail(request, id_character):
#     character = get_object_or_404(Character, id_character=id_character)
#     form=MoveForm()
#     if form.is_valid():
#         ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
#         ancien_lieu.disponibilite = "libre"
#         ancien_lieu.save()
#         form.save()
#         nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
#         nouveau_lieu.disponibilite = "occupé"
#         nouveau_lieu.save()
#         return redirect('character_detail', id_character=id_character)
#     else:
#         form = MoveForm()
#         lieu = character.lieu
#         return render(request,
#                   'playground/character_detail.html',
#                   {'character': character, 'lieu': lieu, 'form': form})
    

    """
    Quand l'utilisateur accède à la page pour la première fois (méthode GET) :

    Un formulaire vide est affiché, permettant à l'utilisateur de saisir des données.
    Ce cas est géré dans la partie else, car il s'exécute lorsque la méthode n'est pas POST.

Quand l'utilisateur soumet le formulaire (méthode POST) :

    Les données du formulaire sont récupérées et utilisées pour mettre à jour les objets correspondants (comme le Character et les Equipement).
    Ce cas est géré dans la partie if request.method == "POST", car elle s'exécute uniquement lorsque la méthode est POST.
    """

from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, Equipement
from .forms import MoveForm

def character_detail(request, id_character):
    # Étape 1 : Récupérer le personnage en question
    character = get_object_or_404(Character, id_character=id_character)
    
    # Étape 2 : Vérifier si la requête est de type POST
    if request.method == "POST":
        # Créer un formulaire avec les données soumises
        form = MoveForm(request.POST, instance=character)
        
        if form.is_valid():  # Vérifier si le formulaire est valide
            # 1. Mettre à jour l'ancien lieu
            ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            ancien_lieu.disponibilite = "libre"
            ancien_lieu.save()
            
            # 2. Sauvegarder le personnage avec les nouvelles données
            form.save()
            
            # 3. Mettre à jour le nouveau lieu
            nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            nouveau_lieu.disponibilite = "occupé"
            nouveau_lieu.save()
            
            # 4. Rediriger vers la page mise à jour
            return redirect('character_detail', id_character=id_character)
    
    else:  # Cas où la requête est GET
        # Créer un formulaire vide pour l'affichage
        form = MoveForm()

    # Étape 3 : Rendre le template avec les données appropriées
    return render(request, 'blog/character_detail.html', {
        'character': character,
        'form': form
    })
