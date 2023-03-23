from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView,
    DetailView, UpdateView, 
    DeleteView, TemplateView
)
from .models import Product, Supplier

# Create your views here.


class InicioView(TemplateView):
    template_name = "index.html"


''' PRODUCTS '''


class ProductListView(ListView):
    model = Product
    template_name = "products/list_products.html"


class ProductByKeyListView(ListView):
    template_name = "products/search_product.html"

    def get_queryset(self):
        key_word = self.request.GET.get('kword')
        products = Product.objects.filter(
            name__icontains=key_word
        )
        print(products)
        return products


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/add_product.html"
    fields = '__all__'

    # def clean(self):
    #     buy_price = self.cleaned_data.get('buy_price')
    #     sell_price = self.cleaned_data.get('sell_price')
        
    #     if buy_price < 0 or sell_price < 0:
    #         msg = "El precio no puede ser menor a 0"
    #     return self


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail_product.html"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/update_product.html"
    fields = '__all__'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/delete_product.html"


''' SUPPLIER '''


class SupplierListView(ListView):
    model = Supplier
    template_name = "products/list_supplier.html"


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "products/add_supplier.html"
    fields = '__all__'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "products/detail_supplier.html"


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "products/update_supplier.html"
    fields = '__all__'


