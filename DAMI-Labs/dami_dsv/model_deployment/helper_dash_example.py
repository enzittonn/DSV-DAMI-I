#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : luis-eduardo@dsv.su.se
# Created Date: 2020/06/30
# =============================================================================
"""
Creation of HTML webpage with Dash and visualization with Plotly.
This file is called from the `dash_example_web.py`, and its main goal
is to make the main code more readable.
"""
# =============================================================================
# Imports
# =============================================================================

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px

from pathlib import Path
import pandas as pd


# =============================================================================
# Functions
# =============================================================================

def update_histogram(colname = None, sample=None):
    """
    Draws a histogram plot from the original dataset and puts the value
    from the `sample` that the user has input in the website.
    """
    fig = px.histogram(data,
                    x=colname,
                    color="target",
                    labels={k:v for k,v in zip(colnames,column_labels)},
                    template="ggplot2")
    fig.update_layout(
        legend = dict(title="Class",
                orientation="h",
                y=1, yanchor="bottom",
                x=0.5, xanchor="center"
                )
    )
    # Show a black line with the current value of the sample
    if (sample is not None):
        fig.add_shape(type="line", line_color="black",
                    line_width = 3, 
                    xref='x', yref='paper',
                    x0 = float(sample[colname]), x1 = float(sample[colname]),
                    y0 = 0, y1 = 1)
    return fig

def update_scatter(col1=None, col2=None, sample=None):
    """
    Draws a scatter plot from the original dataset and puts the value
    from the `sample` that the user has input in the website.
    """
    fig = px.scatter(data,
                    x=col1, 
                    y=col2, 
                    color="target",
                    labels={k:v for k,v in zip(colnames,column_labels)},
                    template="simple_white")

    fig.update_layout(
        legend = dict(
                    title="Class",
                )
    )
     
    if (sample is not None):
        fig.add_annotation( # add a text callout with arrow
            text="SAMPLE!", x=float(sample[col1]), y=float(sample[col2]),
            arrowhead=3, showarrow=True, startarrowsize=3
        )
    return fig

# =============================================================================
# Main
# =============================================================================


#############
"""
Load and simple processing of the original dataset for visualization
purposes in the web application.
"""

# Relative paths respect to current file
# DO NOT MODIFY: Relative path prefix to be able to find the dataset
THIS_FILE_PATH = str(Path(__file__).parent.absolute())+"/"
FOLDER_PATH = THIS_FILE_PATH + "../../datasets/"

# Load original dataset file
dataset_filename = FOLDER_PATH + "seed_data.csv"
data = pd.read_csv(dataset_filename)

# Structure to map df column names to meaningful labels
colnames = data.columns
colnames = colnames.drop('target').values
column_labels = ["Area", "Perimeter", "Compactness", "Length of Kernel",
                "Width of Kernel", "Asymmetry Coeff.", "Length Kernel Groove"]

# Initialization of plots when the website is loaded the first time
fig_histogram = update_histogram("A")
fig_scatter = update_scatter("A","P")

#############
"""
Structure of the HTML webpage using Dash library
"""
app_html_layout = html.Div([

    html.Center(html.H1("DAMI Analytics - Lab Example")),

    html.Div("This app classifies three variaties of wheat seeds from seven real-value attributes extracted from soft X-rays"),

    html.Div(['More information about dataset:', 
        html.A('https://archive.ics.uci.edu/ml/datasets/seeds')
    ]),

    html.H3('Classification with Trained Model'),

    # Create the table to put input values
    html.Table([ html.Tbody([
        # Area
        html.Tr([
            html.Td( html.B('Area (A):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-A',
                    min=10,
                    max=22,
                    step=0.2,
                    value=14,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-A',children=''), style={'width':'10%'} ),
            ]),
        # Perimeter
        html.Tr([
            html.Td( html.B('Perimeter (P):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-P',
                    min=10,
                    max=20,
                    step=0.2,
                    value=14,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-P',children=''), style={'width':'20%'} ),
            ]),
        # Compactness
        html.Tr([
            html.Td( html.B('Compactness (C):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-C',
                    min=0.8,
                    max=1.0,
                    step=0.005,
                    value=0.875,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-C',children=''), style={'width':'20%'} ),
            ]),
        # Length of Kernel LK
        html.Tr([
            html.Td( html.B('Length of Kernel (LK):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-LK',
                    min=4,
                    max=7,
                    step=0.05,
                    value=5.5,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-LK',children=''), style={'width':'20%'} ),
            ]),
        # Width of Kernel WK
        html.Tr([
            html.Td( html.B('Width of kernel (WK):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-WK',
                    min=2,
                    max=4,
                    step=0.05,
                    value=3.2,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-WK',children=''), style={'width':'20%'} ),
            ]),
        # Asymmetry Coeff A_Coef
        html.Tr([
            html.Td( html.B('Asymmetry Coeff (A_Coef):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-A_Coef',
                    min=0,
                    max=10,
                    step=0.2,
                    value=3.6,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-A_Coef',children=''), style={'width':'20%'} ),
            ]),
        # Length Kernel Groove LKG
        html.Tr([
            html.Td( html.B('Length of kernel Groove (LKG):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-LKG',
                    min=4,
                    max=8,
                    step=0.1,
                    value=5.2,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-LKG',children=''), style={'width':'20%'} ),
            ]),
        ]), 
    ], style={'width':'100%', 'padding':'0', 'margin':'0'}),

    html.Center( 
        html.Div([
            html.Br(),
            html.H4(html.B('Classification result', id='classification-result', style={'color':'#983e0f'})),
            html.Button('Execute Classification', id='submit', style={'margin':'0 auto', 'width':'30%'}),
        ])
    ),

    html.Br(),

    html.Center(html.B('Possible classes: [0:Kama], [1:Rosa], [2:Canadian]', style={'color':'blue'})),

    html.Hr(),

    html.H3('Dataset Visualization'),

    html.Div('The next plots show some characteristics of the original dataset. Note that the values from the SAMPLE that was input above will be highlighted in the plot according to the selected variables.'),

    # Layout for plots
    html.Table([
        html.Tbody([
            # Create the cell for the first plot
            html.Tr([
                html.Td([
                    
                    html.H5('Histogram per class of a variable'),

                    html.Label("Choose a variable:"),

                    dcc.Dropdown(id='dropdown-histogram',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='A'
                    ),

                    dcc.Graph(
                        id='graph-histogram',
                        figure = fig_histogram
                    ),
                ], style={'width':'40%'} ),

                html.Td([
                    
                    html.H5('Scatter plot of two variables'),

                    html.Label("Choose two variables to plot:"),

                    dcc.Dropdown(id='dropdown-scatter-1',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='A'
                    ),

                    dcc.Dropdown(id='dropdown-scatter-2',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='P'
                    ),

                    dcc.Graph(
                        id='graph-scatter',
                        figure = fig_scatter
                    ),
                ], style={'width':'60%'} )
            ])
        ])
    ], style={'width': '100%'}),
    
], style={'columnCount': 1})