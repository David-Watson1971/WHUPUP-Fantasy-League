import pandas as pd
import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/season_points', name="Season Points")

####################### DATASET #############################
df2 = pd.read_excel('WHUPUP.xlsx', sheet_name='Cumulative Points')

####################### BAR CHART #############################
linefig =  px.line(df2, 
                   x="Gameweek", 
                   y='Total Points', 
                   color='Fantasy Team',
                   title='Accumulated Points over the Season',
                   template='plotly_dark'
                   )

####################### PAGE LAYOUT #############################
layout = html.Div([
    dbc.Row(
        [dbc.Col(
            [dcc.Graph(figure=linefig)]
        )]
    )
])

