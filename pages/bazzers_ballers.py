import pandas as pd
import dash
from dash import dcc, html, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
from dash.dependencies import Input, Output

template_theme2 = "flatly"
template_theme1 = "darkly"

dash.register_page(__name__, path='/bazzers_ballers', name="Bazzers Ballers")


df = pd.read_excel('WHUPUP.xlsx', sheet_name='Weekly Points')
df2 = df[df['Fantasy Team'].isin(['Bazzers Ballers'])]
##df3 = pd.read_excel('WHUPUP.xlsx', sheet_name='Bazzers Ballers')


####################### BAR CHART #############################
histfig = px.histogram(df2,
                       x='Gameweek',
                       y='Points',
                       color='Player Position',
                       title='Bazzers Ballers: Weekly Points per Position',
                       template='plotly_dark'
                       )

piefig = px.pie(df2, 
                names='Player Position', 
                values='Points',
                color='Player Position',
                hole=.5,
                title='Bazzers Ballers: Breakdown of Total Points per Position',
                template='plotly_dark')




####################### PAGE LAYOUT #############################

layout = html.Div([
    dbc.Row(
        [dbc.Col(
            [dcc.Graph(figure=histfig)]
        )]

    ),
    dbc.Row(
        [dbc.Col(
            [dcc.Graph(figure=piefig)]
        )]
    )
    
])