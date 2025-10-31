from django.contrib import admin
from django.http import HttpResponse
import csv
from datetime import datetime
from .models import Contacto

def export_contactos_csv(modeladmin, request, queryset):
    # usamos modeladmin para obtener los campos y request para el nombre del archivo
    meta = modeladmin.model._meta
    # lista fija para mantener orden y sólo incluir los campos que quieres
    field_names = ['id', 'nombre', 'correo', 'telefono', 'direccion']

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    user = request.user.username if request.user.is_authenticated else "anon"
    filename = f"contactos_{user}_{timestamp}.csv"

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    response.write('\ufeff')  
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([str(getattr(obj, f, '')) for f in field_names])
    return response
export_contactos_csv.short_description = "Exportar seleccionados a CSV"

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono', 'direccion')
    search_fields = ('nombre', 'correo')
    actions = [export_contactos_csv]

admin.site.register(Contacto, ContactoAdmin)

