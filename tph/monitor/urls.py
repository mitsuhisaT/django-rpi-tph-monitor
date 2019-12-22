"""
Urls definitions.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from django.urls import include, path
from rest_framework import routers
from monitor import views

router = routers.DefaultRouter()
router.register(r'BME280', views.BME280ViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.show, name='show'),
    path('showlastmonth', views.showlastmonth, name='showlastmonth'),
    path('tasks/<int:rpt>/<int:untl>', views.tasks, name='tasks'),
    path('rest/', include(router.urls)),
    path('api_auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
