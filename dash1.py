# Import Dash Libraries
import dash
from dash import html
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import researchpy as rp

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('/Users/RyanMburu/Documents/DS-Projects/Supervised-Learning/Parkinsons/Clean Parkinsons (1).csv')

list_gender = list(df['Gender'].unique())


# Information cards
card_age = dbc.Card(
    [
        dbc.CardHeader('Most Popular Age group suffering From Parkinsons is :'),
        dbc.CardBody(
            [
                html.P('73')
            ]
        )
    ], color='#DEDEDE',
)

card_gender = dbc.Card(
    [
        dbc.CardHeader('Most Popular Gender suffering From Parkinsons is :'),
        dbc.CardBody(
            [
                html.P('Male')
            ]
        )
    ], color='#DEDEDE',
)




# Deck for the cards
cards1 = dbc.CardDeck(
    [
        dbc.Col(card_age, width='auto'),
        dbc.Col(card_gender, width='auto')
    ],
)

# Dropdowns
gender_dropdown = dbc.Card(
    [
        html.Div(
            [
                dbc.Label('Chose the Gender of your patient : '),
                dcc.Dropdown(
                    id = 'age_dropdown',
                    options = [{'label' : i, 'value':i} for i in list_gender],
                    value='Age'
                ),
            ]
        )
    ], body=True, color='dark', outline=True
)

# User Inputs

# Age

age_input = dbc.Card(
    [
        html.Div(
            [
                dbc.Label('Whats the patients age ? : '),
                dcc.Input(
                    id = 'age_input',
                    placeholder = 'Age : ',
                    type = 'number',
                ),
                html.Br(),
            ]
        )
    ], body=True, color='dark', outline=True
)

# Tremors
list_tremors = list(df['Tremor'].unique())

tremor_dropdown = dbc.Card(
    [
        html.Div(
            [
                dbc.Label('Is the patient experiencing tremors ? : '),
                dcc.Dropdown(
                    id = 'tremor_dropdown',
                    options = [{'label' : i, 'value':i} for i in list_tremors],
                    value='Tremor'
                ),
            ]
        )
    ], body=True, color='dark', outline=True
)

# History in the Family
list_history = list(df['History'].unique())

history_dropdown = dbc.Card(
    [
        html.Div(
            [
                dbc.Label('History in the family? : '),
                dcc.Dropdown(
                    id = 'history_dropdown',
                    options = [{'label' : i, 'value':i} for i in list_history],
                    value='History'
                ),
            ]
        )
    ], body=True, color='dark', outline=True
)

# Deck with info input on age, gender, history in fam and presence of tremors

cards2 = dbc.CardDeck(
    [
        dbc.Col(age_input, width='auto'),
        dbc.Col(gender_dropdown, width='auto'),
        dbc.Col(tremor_dropdown, width='auto'),
        dbc.Col(history_dropdown, width='auto'),
    ],
)

# App layout
app.layout = dbc.Container(
    # Title
    [
        html.H1(
            'PARKINSONS PREDICTOR'
        ),
        html.Hr(),

        #Info cards
        dbc.Row(
            [
                html.Div([cards1])
            ]
        ),
        html.Hr(),

        html.H1(
            'Patients General Information '
        ),
        html.Hr(),
        #DropDowns

        dbc.Row(
            [
                html.Div([cards2])
            ]
        ),
        html.Hr(),

    ], fluid=True
)



# Call the app
if __name__ == '__main__':
    app.run_server(debug=True)