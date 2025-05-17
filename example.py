import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_gauge_component.gauge as gauge

# Initialize the Dash app
app = dash.Dash(__name__)

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

        # Multi-color Gauge Example
        html.Div([
            html.H2("Multi-color Gauge", style={'textAlign': 'center'}),
            html.P("Gauge with multiple color ranges", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="multi-color-gauge",
                min_value=0,
                max_value=100,
                value=42,
                width="100%",
                height="100%",
                color_ranges=[
                    {'min': 0, 'max': 25, 'color': '#FF0000'},  # Red
                    {'min': 25, 'max': 75, 'color': '#FFFF00'},  # Yellow
                    {'min': 75, 'max': 100, 'color': '#00FF00'},  # Green
                ],
                gauge_thickness=0.1
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
                height="100%", # Equal height for a perfect circle
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
                color_ranges=[
                    {'min': 0, 'max': 10, 'color': '#FF0000'},   # Red
                    {'min': 10, 'max': 20, 'color': '#FF3300'},  # Red-orange
                    {'min': 20, 'max': 30, 'color': '#FF6600'},  # Orange-red
                    {'min': 30, 'max': 40, 'color': '#FF9900'},  # Orange
                    {'min': 40, 'max': 50, 'color': '#FFCC00'},  # Yellow-orange
                    {'min': 50, 'max': 60, 'color': '#FFFF00'},  # Yellow
                    {'min': 60, 'max': 70, 'color': '#CCFF00'},  # Yellow-green
                    {'min': 70, 'max': 80, 'color': '#99FF00'},  # Light green
                    {'min': 80, 'max': 90, 'color': '#66FF00'},  # Green-yellow
                    {'min': 90, 'max': 100, 'color': '#00FF00'}, # Green
                ],
                gauge_thickness=0.5
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
                gauge_thickness=0.5
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8055)
