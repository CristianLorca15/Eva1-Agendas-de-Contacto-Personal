from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q


def inicio(request):
    return render(request, 'AgendaPersonal/inicio.html')

def lista_contactos(request):
    query = request.GET.get('q')
    if query:
        contactos = Contacto.objects.filter(
        Q(nombre__icontains=query) | Q(correo__icontains=query)
        )
    else:
        contactos = Contacto.objects.all()
    return render(request, 'AgendaPersonal/lista_contactos.html', {'contactos': contactos, 'query': query})



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
    return render(request, 'AgendaPersonal/editar_contacto.html', {'form': form, 'contacto': contacto})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'AgendaPersonal/eliminar_contacto.html', {'contacto': contacto})

