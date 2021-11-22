"""
Draw TPH graph.

@date 30 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""

import logging
import re
from datetime import datetime, timedelta
from django.utils import timezone
from django_plotly_dash import DjangoDash
# import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
# from plotly.subplots import make_subplots
from monitor.models import BME280

logger = logging.getLogger(__name__)


chart = DjangoDash('tph_chart',
                   serve_locally=True,
                   )

chart.layout = html.Div(
    id='main',
    children=[
        html.Div(
            dcc.DatePickerRange(
                id='date-picker-range',
                min_date_allowed=datetime(2019, 10, 1),
                max_date_allowed=datetime.now() + timedelta(days=1),
                start_date=datetime.now().replace(
                    hour=0, minute=0, second=0, microsecond=0)
                - timedelta(days=7),
                end_date=datetime.now().replace(
                    hour=23, minute=59, second=59, microsecond=999999)
            ),
        ),
        html.Div(id='tph-chart-div'),
    ],
)


@chart.callback(
    Output('tph-chart-div', 'children'),
    [Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
     ])
def tph_chart_div(*args, **kwargs):  # pylint: disable=unused-argument
    """Call back to generate test data on each change of the dropdown."""
    logger.debug('start')
    logger.debug(f'timezone: {timezone.now()}, datetime: {datetime.now()}')
    logger.debug(f'args: {args}')
    # FIXME use locale and correct rime zoone.
    sdt = re.sub('00$', '00+09:00', args[0])
    edt = re.sub('999999', '999999+09:00', args[1])
    logger.debug(f'start date: {sdt}, end date: {edt}')
    logger.debug(f'kwargs: {kwargs}')
    bme280s = BME280.objects.filter(measure_date__range=(sdt, edt))
    logger.debug(f'bme280s.count: {len(bme280s)}')
    t = [bme280.temperature for bme280 in bme280s]
    p = [bme280.pressure for bme280 in bme280s]
    h = [bme280.humidity for bme280 in bme280s]
    mdt = [bme280.measure_date for bme280 in bme280s]
    logger.debug(f'temperature: {t[0]}')

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=mdt, y=t, name='temperature(C)'),
    )
    fig.add_trace(
        go.Scatter(x=mdt, y=p, name='pressure(hPa)', yaxis='y2'),
    )
    fig.add_trace(
        go.Scatter(x=mdt, y=h, name='humidity(%)', yaxis='y3'),
    )

    fig.update_layout(
        title_text='Stored temperature, pressure and humidity from BME280',
        width=1050,
        height=600,
        xaxis={
            'domain': [0, 0.9],
            'title': 'Date(UTC)'
        },
        yaxis={
            'title': 'temperature(C)',
            'titlefont': {'color': 'navy'},
            'tickfont': {'color': 'navy'},
        },
        yaxis2={
            'title': 'pressure(hPa)',
            'titlefont': {'color': 'coral'},
            'tickfont': {'color': 'coral'},
            'anchor': 'x',
            'overlaying': 'y',
            'side': 'right',
        },
        yaxis3={
            'title': 'humidity(%)',
            'titlefont': {'color': 'lime'},
            'tickfont': {'color': 'lime'},
            'anchor': 'free',
            'overlaying': 'y',
            'side': 'right',
            'position': 0.98,
        },
    )

    line_graph = dcc.Graph(
        id='line-area-graph2',
        figure=fig,
        style={'display': 'inline-block', 'width': '100%', 'height': '100%;'},
        )

    logger.debug('end')
    return [line_graph]
