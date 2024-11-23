from django.db import models

# Create your models here.
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200, blank = True)
    def __str__(self):
        return self.id_equip
 
 
class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20, blank = True)
    type = models.CharField(max_length=20, blank = True)
    team = models.CharField(max_length=20, blank = True)
    photo = models.CharField(max_length=200, blank= True)
    image = models.ImageField(upload_to='character_images/', null=True, blank=True)  #  image
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.id_character