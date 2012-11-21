from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render_to_response
from django.template import RequestContext
from galeria.models import Imagem, ImagemForm


def show(request):
    imagens = Imagem.objects.all()
    return render_to_response('galeria/galeria.html', {'imagens': imagens },\
            context_instance=RequestContext(request))


class CadastrarImagem(CreateView):
    model = Imagem
    template_name = 'galeria/cadastrar.html'
    success_url = '/galeria/cadastrar/'
    form_class = ImagemForm


class AlterarImagem(UpdateView):
    model = Imagem
    template_name = 'galeria/cadastrar.html'
    success_url = '/galeria/listar/'
    form_class = ImagemForm


class RemoverImagem(DeleteView):
    model = Imagem
    template_name = 'galeria/remover.html'
    success_url = '/galeria/listar/'


class ListarImagem(ListView):
    context_object_name = 'imagens'
    queryset = Imagem.objects.all()
    template_name = 'galeria/listar.html'
