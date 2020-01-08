"""
Urls definitions.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from django.urls import include, path
from rest_framework import routers
from monitor import views
from monitor.views import Bme280List

router = routers.DefaultRouter()
router.register(r'BME280', views.BME280ViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/bme280s', Bme280List.as_view()),
    path('v1/bme280s/<int:year>', Bme280List.as_view()),
    path('v1/bme280s/<int:year>/<int:month>', Bme280List.as_view()),
    path('v1/bme280s/<int:year>/<int:month>/<int:day>', Bme280List.as_view()),
    # path('show', views.show, name='show'),
    # path('show/<int:year>/<int:month>', views.showmonth, name='showmonth'),
    # path('show/<int:year>/<int:month>/<int:day>',
    #      views.showday, name='showday'),
    path('showlastmonth', views.showlastmonth, name='showlastmonth'),
    path('tasks/<int:rpt>/<int:untl>', views.tasks, name='tasks'),
    path('rest/', include(router.urls)),
    path('api_auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
