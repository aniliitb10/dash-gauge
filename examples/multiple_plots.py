import dash
from dash import html

import dash_gauge_component.gauge as gauge
from examples.util import Util

# Initialize the Dash app
app = dash.Dash(__name__)

# Expose the server variable for Gunicorn
server = app.server

# Define the app layout
app.layout = html.Div([
    html.H1("Dash Gauge Component Examples", style={'textAlign': 'center', 'marginBottom': '30px'}),

    html.Div([
        # Basic Gauge Example
        html.Div([
            html.H2("Basic Gauge", style={'textAlign': 'center'}),
            html.P("Default gauge with bottom-left to bottom-right arc", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="basic-gauge",
                min_value=0,
                max_value=100,
                value=75,
                width="100%",
                height="100%",
                gauge_thickness=0.1  # Thinner, more elegant gauge
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),

        # Multicolor Gauge Example
        html.Div([
            html.H2("Multi-color Gauge", style={'textAlign': 'center'}),
            html.P("Gauge with multiple color ranges", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="multi-color-gauge",
                min_value=0,
                max_value=100,
                value=94,
                width="100%",
                height="100%",
                color_ranges=[
                    {'min': 0, 'max': 33, 'color': '#FF0000'},  # Red
                    {'min': 33, 'max': 67, 'color': '#FFFF00'},  # Yellow
                    {'min': 67, 'max': 100, 'color': '#00FF00'},  # Green
                ],
                gauge_thickness=1,
                needle_thickness=12,

                show_value=True,
                value_format="{:.0f}%",
                value_font_size=25,
                value_font_family='Numbers',
                value_font_color='auto',

                tick_font_size=16,
                tick_font_color='#666666',
                tick_label_radius=1.2,
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),

    html.Div([
        # Square/Circle Gauge Example (Equal width and height)
        html.Div([
            html.H2("Square/Circle Gauge", style={'textAlign': 'center'}),
            html.P("Equal width and height (100% × 100%) for perfect circle", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="square-gauge",
                min_value=0,
                max_value=100,
                value=60,
                width="100%",  # Percentage-based width
                height="100%",  # Equal height for a perfect circle
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),

        # Custom Angle Gauge Example
        html.Div([
            html.H2("Custom Angle Gauge", style={'textAlign': 'center'}),
            html.P("Custom start and end angles (-90° to 90°)", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="custom-angle-gauge",
                min_value=0,
                max_value=100,
                value=60,
                width="100%",
                height="100%",
                start_angle=-90,
                end_angle=90,
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),

    html.Div([
        # Smooth Gradient Gauge Example
        html.Div([
            html.H2("Smooth Gradient Gauge", style={'textAlign': 'center'}),
            html.P("Smooth color gradient from red (0) to green (100)", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="gradient-gauge",
                min_value=0,
                max_value=100,
                value=90,
                width="100%",
                height="100%",
                color_ranges=Util.generate_gradient_colors('#FF0000', '#00FF00', 4, 0.0, 100.0),
                gauge_thickness=0.5,
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),

        # Custom Needle Gauge Example
        html.Div([
            html.H2("Custom Needle Gauge", style={'textAlign': 'center'}),
            html.P("Custom needle color and thickness", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="custom-needle-gauge",
                min_value=0,
                max_value=100,
                value=85,
                width="100%",
                height="100%",
                needle_color="#FF5733",
                needle_thickness=4.0,
                gauge_thickness=0.5,
                show_value=False,
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8055)
