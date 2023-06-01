from django.shortcuts import render
from .forms import JeuxVideosForm
from . import models

def index(request):
    return render(request, 'jeux_video/index.html')

def bonjour(request):
    nom=request.GET["nom"]
    return render(request,'jeux_video/bonjour.html',{"nom":nom})

def ajout(request):
    if request.method == "POST":
        form = JeuxVideosForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request,"/jeux_videos/ajout.html",{"jeuxvideos" : jeuxvideos})
        else:
                return render(request,"jeux_video/ajout.html",{"form": form})
    else :
        form = JeuxVideoForm() # création d'un formulaire vide
        return render(request,"jeux_video/ajout.html",{"form" : form})

def formulaire(request):
        return render(request, 'jeux_video/formulaire.html')