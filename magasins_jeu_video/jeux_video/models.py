from django.db import models

# Create your models here.


from django.db import models

class JeuxVideos(models.Model):
    nom = models.CharField(max_length=100)
    developper = models.CharField(max_length = 100)
    date_de_sortie = models.DateField(blank=True, null = True)
    resume = models.IntegerField(blank=False)
    titre = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.titre} développé par {self.developper} sorti le{self.date_de_sortie}"
        return chaine