import pandas as pd 
import os
from dash import dcc
from dash import html
import plotly.graph_objs as go
import dash.dependencies as ddep
import dash_bootstrap_components as dbc
import plotly.express as px

from app import app, db

mypath = os.getcwd()

EURONEXT = os.path.join(mypath,"euronext")
BOURSE = os.path.join(mypath,"bourse")
for file in os.listdir(EURONEXT):
    path = os.path.join(EURONEXT, file)
    if(file.endswith(".xlsx")):
        print(f"Loading {path}")
        df = pd.read_excel(path)
        break

html_table = df.to_html(classes="table table-bordered")

tab2_layout = html.Div([
    html.H2("AAAAAAAAAAAAA"),
    html.Div([html.Table([html.Tr([html.Th(col) for col in df.columns])] + 
                        [html.Tr([html.Td(cell) for cell in row]) for row in df.values])])
])

