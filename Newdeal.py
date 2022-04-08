#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lordyuyox

# Graficador de datos del Survey SHINING

import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objs as go
#Functions

def Jy_to_ergs(cont1, cont2):
        FIR = 7.98*10**(-15)*(4.67*cont1 + cont2)
        return FIR

def generate_table(dataframe, max_rows=30):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('resolvedmaps_fluxes - Table6_MRF(update).csv')


fig1 = px.scatter(df, x='Luminosity(log)', y='NIII57/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=True, title='Luminosity vs. NIII57/FIR')



app.layout = html.Div(children=[
    html.H1(children='SHINING Survey Data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.H4(children='SHINING Survey Data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    generate_table(df),

    html.Div(children='''
        The data used in the development of the paper: 
        SHINING, A Survey of Far Infrared Lines in Nearby Galaxies. I: Survey Description, Observational Trends, and Line Diagnostics &
        SHINING, A Survey of Far Infrared Lines in Nearby Galaxies. II: Line-Deficit Models, AGN impact, [CII]-SFR Scaling Relations, and Mass-Metallicity Relation in (U)LIRGS
    '''
    ),
    dcc.Dropdown(
        id="dropdown",
        options=['NIII57/FIR', 'OI63/FIR', 'OIII88/FIR', 'NII122/FIR', 'OI145/FIR', 'CII158/FIR'],
        value=['Luminosity(log)', 'Brightness (log)'],
        multi=False
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig1
        ),
    html.P('Filter by Distance in Mpc_'),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=600, step=1,
        marks={0: '0', 600: '600'},
        value=[0.0, 600]
    )
])





@app.callback(
    Output("example-graph","figure"),
    Input("range-slider", "value"),
)


def update_bar_chart(slider_range):
    df = pd.read_csv('resolvedmaps_fluxes - Table6_MRF(update).csv')
    low, high = slider_range
    mask = (df['DL[Mpc]'] > low) & (df['DL[Mpc]'] < high)
    fig1 = px.scatter(df[mask], x='Luminosity(log)', y='NIII57/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=True, title='Luminosity vs. NIII57/FIR')
    fig1.update_layout(
    legend=dict(
        x=0,
        y=0,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
        ),
    xaxis=dict(
        type='log'
        ),
    yaxis=dict(
        type='log'
        ),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
    return fig1


if __name__ == '__main__':
    app.run_server(debug=True)
