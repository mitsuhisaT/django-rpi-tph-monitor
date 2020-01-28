"""
Urls definitions.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
# from monitor import views
from monitor.views import Bme280List, BME280ViewSet
from monitor.views import index, showlastmonth, tph_chart_view, tasks
import monitor.tph_chart


router = routers.DefaultRouter()
router.register(r'BME280', BME280ViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('v1/bme280s', Bme280List.as_view()),
    path('v1/bme280s/<int:year>', Bme280List.as_view()),
    path('v1/bme280s/<int:year>/<int:month>', Bme280List.as_view()),
    path('v1/bme280s/<int:year>/<int:month>/<int:day>', Bme280List.as_view()),
    # path('show', views.show, name='show'),
    # path('show/<int:year>/<int:month>', views.showmonth, name='showmonth'),
    # path('show/<int:year>/<int:month>/<int:day>',
    #      views.showday, name='showday'),
    path('showlastmonth', showlastmonth, name='showlastmonth'),
    path('chart', tph_chart_view, name="tph_chart"),
    path('tasks/<int:rpt>/<int:untl>', tasks, name='tasks'),
    path('rest/', include(router.urls)),
    path('api_auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
