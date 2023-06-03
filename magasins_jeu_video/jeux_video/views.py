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
            JeuxVideos = form.save()
            return render(request,"jeux_videos/ajout.html",{"jeuxvideos" : jeuxvideos})
        else:
                return render(request,"jeux_video/ajout.html",{"form": form})
    else :
        form = JeuxVideoForm() # création d'un formulaire vide
        return render(request,"jeux_video/ajout.html",{"form" : form})


def traitement(request):
    lform = JeuxVideosForm(request.POST)
    if lform.is_valid():
        JeuxVideos = lform.save()
        return render(request, "mesmineraux/affiche.html", {"jeux_video": jeux_videos})
    else:
        return render(request, "mesmineraux/ajout.html", {"form": lform})


def affiche(request, id):
    JeuxVideos = models.mesmineraux.objects.get(pk=id)
    return render(request, "jeux_video/affiche.html", {"jeux_video": jeux_videos})


def delete(request, id):
    suppr = models.jeux_video.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/mesmineraux/index/", )


def update(request, id):
    pierre = models.jeux_video.objects.get(pk=id)
    aform = JeuxVideosForm(jeux_video.dic())
    return render(request, "jeux_video/ajoutupdate.html/", {"form": aform, "id": id})

def updatetraitement(request, id):
    aform = JeuxVideosForm(request.POST)
    saveid = id
    if aform.is_valid():
        jeux_video = aform.save(commit = False)
        jeux_video.id = saveid
        jeux_video.save()
        return HttpResponseRedirect("/mesmineraux/index/")
    else:
        return render(request, "mesmineraux/ajoutupdate.html", {"form": aform})