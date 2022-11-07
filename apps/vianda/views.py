from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from apps.vianda.forms import ViandaForm
from apps.vianda.models import Vianda

@login_required(login_url='usuarios:login')
@permission_required('vianda.add_vianda', login_url="usuario:login")
def registrar_vianda(request):

    if request.method == 'POST':
        vianda_form = ViandaForm(request.POST)

        if vianda_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            vianda_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la vianda')
            return redirect(reverse('vianda:registrar_vianda'))
    else:
        vianda_form = ViandaForm()

    return render(request, 'vianda/registrarVianda.html',
                  {'form': vianda_form})


@login_required(login_url='usuarios:login')
@permission_required('vianda.view_vianda', login_url="usuario:login")
def listar_vianda(request):
    viandas = Vianda.objects.all()
    return render(request, 'vianda/listarVianda.html',
                  {'viandas': viandas})