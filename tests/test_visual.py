import dash
from dash import html
import dash_gauge_component.gauge as gauge

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Gauge Visual Test", style={'textAlign': 'center', 'marginBottom': '30px'}),

    html.Div([
        # Test 1: Equal width and height for circular appearance
        html.Div([
            html.H2("Circular Gauge Test", style={'textAlign': 'center'}),
            html.P("Equal width and height (100% × 100%) for perfect circle", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="circular-gauge",
                min_value=0,
                max_value=100,
                value=50,
                width="100%",  # Percentage-based width
                height="100%", # Equal height for perfect circle
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),

        # Test 2: Default angles (bottom left to bottom right)
        html.Div([
            html.H2("Default Angles Test", style={'textAlign': 'center'}),
            html.P("Default angles (225° to -45°) - starts bottom left, ends bottom right", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="default-angles-gauge",
                min_value=0,
                max_value=100,
                value=50,
                width="100%",
                height="100%",
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),

    html.Div([
        # Test 3: Smooth gradient test
        html.Div([
            html.H2("Smooth Gradient Test", style={'textAlign': 'center'}),
            html.P("Smooth color gradient from red (0) to green (100)", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="smooth-gradient-gauge",
                min_value=0,
                max_value=100,
                value=75,
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

        # Test 4: All features combined
        html.Div([
            html.H2("All Features Test", style={'textAlign': 'center'}),
            html.P("Combining all improvements", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="all-features-gauge",
                min_value=0,
                max_value=100,
                value=60,
                width="100%",
                height="100%",
                color_ranges=[
                    {'min': 0, 'max': 30, 'color': '#FF0000'},  # Red
                    {'min': 30, 'max': 70, 'color': '#FFFF00'},  # Yellow
                    {'min': 70, 'max': 100, 'color': '#00FF00'},  # Green
                ],
                needle_color="#FF5733",
                needle_thickness=4.0,
                gauge_thickness=0.5
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8056)