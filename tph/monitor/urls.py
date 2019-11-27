from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.show, name='show'),
    path('bsstest/<int:bss_id>', views.bsstest, name='bsstest'),
]
