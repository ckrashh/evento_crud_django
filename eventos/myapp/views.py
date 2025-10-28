from django.shortcuts import render
from .models import Evento, Voluntario
from .forms import EventoForm, VoluntarioForm
from .mixins import CRUDMixin

class EventoView(CRUDMixin):
    template_name = 'eventos.html'
    model = Evento
    form_class = EventoForm
    search_fields = ['titulo', 'descripcion']
    paginate_by = 5
    context_object_name = 'eventos'
    success_url = 'eventos'
    order_by = '-fecha'

class VoluntarioView(CRUDMixin):
    template_name = 'voluntarios.html'
    model = Voluntario
    form_class = VoluntarioForm
    search_fields = ['nombre', 'email', 'telefono']
    paginate_by = 5
    context_object_name = 'voluntarios'
    success_url = 'voluntarios'
    order_by = '-id'

def index(request):
    return render(request, 'index.html')