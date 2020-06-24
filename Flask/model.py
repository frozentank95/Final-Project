import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
from dash.dependencies import Input, Output, State
import pickle
import numpy as np

tips = sns.load_dataset("tips")
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

loadModel = pickle.load(open('tips_lm_model.sav', 'rb'))

app.layout = html.Div(children = [
    html.Div(children=[
                html.Div([
                    html.P('Total Bill'),
                    dcc.Input(id='s_total_bill',
                    type='number',
                    value='total_bill')
                ],className='row col-3')
            ]),
    html.Br(),
    html.Div(children=[
                html.Div([
                    html.P('Size'),
                    dcc.Input(id='s_size',
                    type='number',
                    value='size')
                ],className='row col-3')
            ]),
    html.Br(),
    html.Div(id='display-selected-values')
])

@app.callback(
    Output('display-selected-values', 'children'),
    [Input('s_total_bill', 'value'),
     Input('s_size', 'value')])
def set_display_children(total_bill, size):
    file = []
    file.append(total_bill)
    file.append(size)
    file1 = np.array(file)
    loadModel = pickle.load(open('tips_lm_model.sav', 'rb'))
    return 'Perkiraan tips adalah {}'.format(loadModel.predict(file1.reshape(1,2)))

if __name__ == '__main__':
    app.run_server(debug=True)