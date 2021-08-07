from django.urls import path
from producto.views import CreateProduct, ListProducts, ProductOwner, Products, UpdateProduct
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Products, name="products"),
    path('ListProducts', ListProducts, name="ListProducts"),
    path('register', CreateProduct),
    path('update', UpdateProduct),
    path('addOwner', ProductOwner),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)