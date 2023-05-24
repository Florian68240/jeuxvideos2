from django.shortcuts import render
from .forms import JeuxVideoForm
from . import models

def index(request):
    return render(request, 'jeux_video/index.html')

def bonjour(request):
    nom=request.GET["nom"]
    return render(request,'jeux_video/bonjour.html',{"nom":nom})

def ajout(request):
    if request.method == "POST":
        form = JeuxVideoForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request,"/bibliotheque/affiche.html",{"livre" : livre})
        else:
                return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = JeuxVideoForm() # création d'un formulaire vide
        return render(request,"bibliotheque/ajout.html",{"form" : form})
