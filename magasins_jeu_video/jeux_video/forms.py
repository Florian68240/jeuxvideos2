from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class JeuxVideoForm(ModelForm):
    class Meta:
        model = models.JeuxVideo
        fields = ('nom', 'developper', 'date_sortie', 'prix','titre')
        labels = {
            'nom' : _('Nom'),
            'developper' : _('Developpeur') ,
            'date_sortie' : _('Date␣de␣sortie'),
            'prix' : _('Prix'),
            'titre' : _('Titre')
}