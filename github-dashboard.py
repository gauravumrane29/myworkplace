import plotly.express as px
import pandas as pd  # Import pandas

# Sample data
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# Create a Plotly figure
fig = px.bar(df, x='Category', y='Values', title='Sample Bar Chart')

# Save the figure as an HTML file
fig.write_html('dashboard.html')
