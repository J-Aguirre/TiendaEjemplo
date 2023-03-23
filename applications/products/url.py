from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.ProductListView.as_view(),
        name='list_products'        
    ),
    path(
        'search-product/',
        views.ProductByKeyListView.as_view(),
        name='search_product'
    ),
    path(
        'add-product/',
        views.ProductCreateView.as_view(),
        name='add_product'
    ),
    path(
        'detail-product/<pk>',
        views.ProductDetailView.as_view(),
        name='detail_product'
    ),
    path(
        'update-product/<pk>',
        views.ProductUpdateView.as_view(),
        name='update-product'
    ),
    path(
        'delete-product/<pk>',
        views.ProductDeleteView.as_view(),
        name='delete-product'
    ),
    path(
        'list-supplier/',
        views.SupplierListView.as_view(),
        name='list_supplier'
    ),
    path(
        'add-supplier/',
        views.SupplierCreateView.as_view(),
        name='add-supplier'
    ),
    path(
        'detail-supplier/<pk>',
        views.SupplierDetailView.as_view(),
        name='detail_supplier'
    ),
    path(
        'update-supplier/<pk>',
        views.SupplierUpdateView.as_view(),
        name='update_supplier'
    ),
]