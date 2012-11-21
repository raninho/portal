from django.db import models
from django.forms import ModelForm

class Imagem(models.Model):
    descricao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='galeria')

    class Meta:
        db_table = 'Imagens'

    def __unicode__(self):
        return self.descricao

    @models.permalink
    def get_url_alterar(self):
        return ('alterar-imagem', [str(self.id)])

    @models.permalink
    def get_url_remover(self):
        return ('remover-imagem', [str(self.id)])

class ImagemForm(ModelForm):
    class Meta:
        exclude = ('id')
        model = Imagem
