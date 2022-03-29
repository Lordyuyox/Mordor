#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lordyuyox

# Graficador de datos del Survey SHINING

import csv 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
#from dash import dash_html_components as html
from dash.dependencies import Input, Output

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
fig2 = px.scatter(df, x='Luminosity(log)', y='OI63/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=False, title='Luminosity vs. OI63/FIR')
fig3 = px.scatter(df, x='Luminosity(log)', y='OIII88/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=False, title='Luminosity vs. OIII88/FIR')
fig4 = px.scatter(df, x='Luminosity(log)', y='NII122/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=False, title='Luminosity vs. NII122/FIR')
fig5 = px.scatter(df, x='Luminosity(log)', y='OI145/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=False, title='Luminosity vs. OI145/FIR')
fig6 = px.scatter(df, x='Luminosity(log)', y='CII158/FIR', color= 'L_{CO}(log)', symbol= 'Optical_class', hover_name= 'Name', hover_data = ['Brightness (log)', 'DL[Mpc]'], size = 'Redshift', size_max= 100, log_x=True, log_y=False, title='Luminosity vs. CII158/FIR')

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

fig2.update_layout(
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

fig3.update_layout(
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

fig4.update_layout(
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

fig5.update_layout(
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

fig6.update_layout(
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

    html.Div(children=['''
        The data used in the development of the paper: 
        SHINING, A Survey of Far Infrared Lines in Nearby Galaxies. I: Survey Description, Observational Trends, and Line Diagnostics &
        SHINING, A Survey of Far Infrared Lines in Nearby Galaxies. II: Line-Deficit Models, AGN impact, [CII]-SFR Scaling Relations, and Mass-Metallicity Relation in (U)LIRGS
    ''',
    ]),


    dcc.Graph(
        id='example-graph',
        figure=fig1
        )
    ]
)
    
    

if __name__ == '__main__':
    app.run_server(debug=True)
