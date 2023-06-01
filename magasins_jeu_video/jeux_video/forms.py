from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class JeuxVideosForm(ModelForm):
    class Meta:
        model = models.JeuxVideos
        fields = ('nom', 'developper', 'date_sortie', 'prix','type')
        labels = {
            'nom' : _('Nom'),
            'developper' : _('Developpeur') ,
            'date_sortie' : _('Date␣de␣sortie'),
            'prix' : _('Prix'),
            'type' : _('Type')
                }