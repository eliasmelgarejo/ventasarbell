from dal import autocomplete

from stock.models import Linea, Producto


class LineaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Linea.objects.none()

        qs = Linea.objects.all().order_by('-nombre')

        if self.q:
            qs = qs.filter(nombre__startswith=self.q)

        return qs


class ProductoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Producto.objects.none()

        qs = Producto.objects.all().order_by('-nombre')

        if self.q:
            qs = qs.filter(nombre__startswith=self.q)

        return qs


