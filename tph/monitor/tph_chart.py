"""
Draw TPH graph.

@date 30 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import logging
import plotly.graph_objs as go
# import dpd_components as dpd
import numpy as np
from django_plotly_dash import DjangoDash

logger = logging.getLogger(__name__)


chart = DjangoDash(name='tph_chart',
                   serve_locally=True,
                   app_name="TPH chart application"
                   )

chart.layout = html.Div(
    id='main',
    children=[
        html.Div([
            dcc.Dropdown(
                id='select-item',
                options=[{'label': 'all', 'value': 'A'},
                         {'label': 'pressure', 'value': 'P'},
                         {'label': 'humidity', 'value': 'H'},
                         {'label': 'temperature', 'value': 'T'}
                         ],
                value='A',
                className='col-md-12',
                ),
            html.Div(id='tph-chart-div')
            ],
        ),
    ]
)


@chart.callback(
    Output('tph-chart-div', 'children'),
    [Input('select-item', 'value')])
def callback_test(*args, **kwargs):  # pylint: disable=unused-argument
    """Call back to generate test data on each change of the dropdown."""
    logger.debug('start')
    # Creating a random Graph from a Plotly example:
    N = 500
    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    # Create a trace
    trace = go.Scatter(
        x=random_x,
        y=random_y,
        )

    data = [trace]

    layout = dict(
        title='',
        yaxis=dict(zeroline=False, title='Total Expense (£)',),
        xaxis=dict(zeroline=False, title='Date', tickangle=0),
        margin=dict(t=20, b=50, l=50, r=40),
        height=350,
        )

    fig = dict(data=data, layout=layout)
    line_graph = dcc.Graph(
        id='line-area-graph2',
        figure=fig,
        style={'display': 'inline-block', 'width': '100%', 'height': '100%;'},
        )
    children = [line_graph]

    logger.debug('end')
    return children
