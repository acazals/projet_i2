from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('character/<str:id_character>/', views.character_detail, name='character_detail'),
    path('character/<str:id_character>/?<str:message>', views.character_detail, name='character_detail_mes'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
 Comme vous pouvez le voir, nous assignons une vue appelée post_list à l'URL racine. Ce modèle d'URL correspond à une chaîne vide et le résolveur d'URL de Django ignore le nom de domaine (par exemple, http://127.0.0.1:8000/), soit la première partie de l'URL. 
 Ce pattern va donc indiquer à Django d'afficher la vue views.post_list à un utilisateur 
 de votre site web qui se rendrait à l'adresse "http://127.0.0.1:8000/".

La dernière partie, name='post_list', est le nom de l'URL qui sera utilisée afin d'identifier la vue. 
Ce nom peut être le même que celui de la vue ou quelque chose de complètement différent. Plus tard dans ce tutoriel, 
nous allons utiliser les noms que nous avons donné à nos URLs. Il est donc important de donner un nom unique à chaque URL que nous créons.
 Pour vous faciliter la tâche, essayez de trouver des noms d'URLs simple à retenir. 

"""