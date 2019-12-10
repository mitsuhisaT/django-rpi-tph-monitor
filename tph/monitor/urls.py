from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.show, name='show'),
    path('tasks/<int:rpt>/<int:untl>', views.tasks, name='tasks'),
    path('bsstest/<int:bss_id>', views.bsstest, name='bsstest'),
]
