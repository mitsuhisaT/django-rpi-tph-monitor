"""
Draw TPH graph.

@date 30 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""

from datetime import datetime, timedelta
from django.utils import timezone
from django_plotly_dash import DjangoDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import logging
import numpy as np
import plotly.graph_objs as go
import re
from monitor.models import BME280

logger = logging.getLogger(__name__)


chart = DjangoDash(name='tph_chart',
                   serve_locally=True,
                   app_name="TPH chart application"
                   )

chart.layout = html.Div(
    id='main',
    children=[
        html.Div(
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed=datetime(2019, 10, 1),
                max_date_allowed=datetime.now(),
                start_date=datetime.now().replace(
                    hour=0, minute=0, second=0, microsecond=0)
                - timedelta(days=7),
                end_date=datetime.now().replace(
                    hour=23, minute=59, second=59, microsecond=999999)
            ),
        ),
        html.Div(id='tph-chart-div'),
        html.Div(
            dcc.Checklist(
                id='select-item',
                options=[{'label': 'pressure', 'value': 'P'},
                         {'label': 'humidity', 'value': 'H'},
                         {'label': 'temperature', 'value': 'T'}
                         ],
                value=['T', 'H', 'P'],
                labelStyle=['display', 'inline-block']
            ),
        ),
    ],
)


@chart.callback(
    Output('tph-chart-div', 'children'),
    [Input('select-item', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
     ])
def tph_chart_div(*args, **kwargs):  # pylint: disable=unused-argument
    """Call back to generate test data on each change of the dropdown."""
    logger.debug('start')
    logger.debug(f'timezone: {timezone.now()}, datetime: {datetime.now()}')
    logger.debug(f'args: {args}')
    kinds = args[0]
    # FIXME use locale and correct rime zoone.
    sdt = re.sub('00$', '00+09:00', args[1])
    edt = re.sub('999999', '999999+09:00', args[2])
    logger.debug(f'kinds: {kinds}')
    logger.debug(f'start date: {sdt}, end date: {edt}')
    logger.debug(f'kwargs: {kwargs}')
    bme280s = BME280.objects.filter(measure_date__range=(sdt, edt))
    logger.debug(f'bme280s.count: {len(bme280s)}')
    t = [bme280.temperature for bme280 in bme280s]
    p = [bme280.pressure for bme280 in bme280s]
    h = [bme280.humidity for bme280 in bme280s]
    mdt = [bme280.measure_date for bme280 in bme280s]
    logger.debug(f'temperature: {t[0]}')

    data = [go.Scatter(x=mdt, y=t)]
    logger.debug(f'data: {data!r}')

    layout = {
        'title': 'Stored from BME280',
        'yaxis': {'zeroline': False, 'title': 'temperature ()', },
        'xaxis': {'zeroline': False, 'title': 'Date', 'tickangle': 0},
        'margin': {'t': 50, 'b': 50, 'l': 50, 'r': 40},
        'height': 350,
        }

    fig = {'data': data, 'layout': layout}
    line_graph = dcc.Graph(
        id='line-area-graph2',
        figure=fig,
        style={'display': 'inline-block', 'width': '100%', 'height': '100%;'},
        )

    logger.debug('end')
    return [line_graph]
