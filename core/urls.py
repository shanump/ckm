from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('product/<int:pro_id>/', views.product, name='product'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)