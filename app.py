from dash import Dash, html, dcc
import dash
import plotly.express as px
import dash_bootstrap_components as dbc
import openpyxl

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

app.layout = html.Div([
	html.Br(),
	html.P('WHUPUP Fantasy Football League', className="text-dark text-center fw-bold fs-1"),
    html.Div(children=[
	    dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
			  for page in dash.page_registry.values()]
	),
	dash.page_container
], className="col-8 mx-auto")

if __name__ == '__main__':
	app.run(debug=True)