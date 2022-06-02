from django.contrib import admin
from almacen.models import Cliente, Producto, Venta

admin.site.site_header = "Mi almacén"
admin.site.index_title = "Gestión de mi almacén"


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = (
        "nombre",
        "telefono",
    )
    search_fields = [
        "nombre",
        "telefono",
    ]


class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = (
        "nombre",
        "precio",
    )
    search_fields = ["nombre"]


class VentaAdmin(admin.ModelAdmin):
    model = Venta
    list_display = ("id", "cliente", "producto", "fecha")
    date_hierarchy = "fecha"


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
