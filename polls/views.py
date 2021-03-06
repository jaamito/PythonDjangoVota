from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .models import Respuesta,Pregunta,Voto
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'registration/register.html',args)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pregunta.objects.order_by('-dataPubli')[:5]

class PrincipalView(generic.ListView):
    template_name = 'polls/principal.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pregunta.objects.order_by('-dataPubli')[:5]

class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = 'polls/results.html'

def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    try:
        # Id respuesta
        selected_respuesta = pregunta.respuesta_set.get(pk=request.POST['respuesta'])
        #Id usuario
        selected_user = request.POST['user']
        selected_user = int(selected_user)

    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'pregunta': pregunta,
            'error_message': "Tu no has seleccionado una respuesta",
        })
    else:

        v = Voto(author = request.user, respuesta = selected_respuesta)
        v.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(pregunta.id,)))
