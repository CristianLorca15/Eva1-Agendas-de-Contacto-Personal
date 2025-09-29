from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'AgendaPersonal/lista_contactos.html', {'contactos': contactos})

def detalle_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    return render(request, 'AgendaPersonal/detalle_contacto.html', {'contacto': contacto})

def nuevo_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'AgendaPersonal/nuevo_contacto.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'AgendaPersonal/editar_contacto.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'AgendaPersonal/eliminar_contacto.html', {'contacto': contacto})
