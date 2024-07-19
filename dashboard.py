import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# Create a Plotly figure
fig = px.bar(df, x='Category', y='Values', title='Sample Bar Chart')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Dashboard Example'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
