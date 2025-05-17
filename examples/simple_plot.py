import dash
from dash import html
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dash_gauge_component.gauge import Gauge

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Gauge Component Style Examples", style={'textAlign': 'center', 'marginBottom': '30px'}),
    html.Div([
        # All features combined
        html.Div([
            html.H2("All Features Combined", style={'textAlign': 'center'}),
            html.P("Custom styling with color ranges and formatting", style={'textAlign': 'center'}),
            Gauge(
                id="all-features-gauge",
                value=85,
                width="100vw",
                height="100vh",
                color_ranges=[
                    {'min': 0, 'max': 30, 'color': '#FF0000'},  # Red
                    {'min': 30, 'max': 70, 'color': '#FFFF00'},  # Yellow
                    {'min': 70, 'max': 100, 'color': '#00FF00'},  # Green
                ],
                needle_color="#FF5733",
                needle_thickness=4.0,
                gauge_thickness=0.5,
                value_format="{:.0f}%",
                font_family="Helvetica, sans-serif",
                font_size=25,
                font_color="#333333",
                tick_font_size=18,
                tick_font_color="#666666",
            ),
        ], style={'width': '100%', 'margin': '0 auto', 'padding': '10px'}),
    ]),
])

if __name__ == '__main__':
    app.run(debug=True, )
