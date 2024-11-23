from django.contrib import admin
from .models import Character
from .models import Equipement


from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id_character', 'etat', 'lieu', 'image')  # Inclure le champ image
    fields = ('id_character', 'etat', 'lieu', 'image')  # Champs affichés dans le formulaire

# Register your models here.
##admin.site.register(Character)
admin.site.register(Equipement)

# password : Judohkmk-projet15