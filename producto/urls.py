from django.urls import path
from producto.views import CreateProduct, ListProducts, ProductOwner, Products, UpdateProduct

urlpatterns = [
    path('', Products, name="products"),
    path('ListProducts', ListProducts, name="ListProducts"),
    path('register', CreateProduct),
    path('update', UpdateProduct),
    path('addOwner', ProductOwner),
]