"""
Views contoroller.

@date 30 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""
import logging
from datetime import timedelta
from django.conf import settings as ts
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


# @api_view(['GET'])
@csrf_exempt
def tph_chart_view(request, template_name="monitor/chart.html", **kwargs):
    """Create example view.

    that inserts content into the dash context passed to the dash application.
    """
    logger.debug('start')

    context = {
        'site_title': 'TPH monitor',
        'title': 'TPH chart via Plotly Dash for Django.',
        'year': ts.COPYRIGHT_YEAR,
        'owner': ts.OWNER,
    }

    # create some context to send over to Dash:
    dash_context = request.session.get("django_plotly_dash", dict())
    dash_context['django_to_dash_context'] = "I am Dash receiving context from Django"
    request.session['django_plotly_dash'] = dash_context

    logger.debug('end')
    return render(request, template_name=template_name, context=context)
