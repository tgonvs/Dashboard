# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    dcc.Markdown(
        '''
            # Dashboard
            
            Selecione a opção:
        '''
    ),
        
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value='ALL'
    ),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)

def changeText(value):
    if value == 'ALL':
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    elif value == 'MTL':
        return px.bar(df[df['City'] == 'Montreal'], x="Fruit", y="Amount")
    else:
        return px.bar(df[df['City'] == 'SF'], x="Fruit", y="Amount")

if __name__ == '__main__':
    app.run_server(debug=True)
