from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryDetailView, CategoryListView, \
    contacts, VersionCreateView, IndexTemplateView, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),

    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    # path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/',  cache_page(60)(CategoryListView.as_view()), name='category_list'),
    path('category/view/<int:pk>',  ProductListView.as_view(), name='category_view'),
    path('category/edit/<int:pk>',  CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

    path('version/create/', VersionCreateView.as_view(), name='version_create'),
]
