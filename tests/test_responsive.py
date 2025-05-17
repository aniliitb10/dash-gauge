import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_gauge_component.gauge as gauge

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Responsive Gauge Test", style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    html.Div([
        html.P("Resize your browser window to see how the gauges respond. They should scale up when the window increases and scale down when it decreases. The value text should scale proportionally with the gauge.", 
               style={'textAlign': 'center', 'marginBottom': '20px'}),
        
        # Test 1: Percentage-based sizing
        html.Div([
            html.H2("Percentage-based Gauge", style={'textAlign': 'center'}),
            html.P("Width: 100%, Height: 300px", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="percentage-gauge",
                min_value=0,
                max_value=100,
                value=75,
                width="100%",  # Percentage width
                height="300px", # Fixed height
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
        
        # Test 2: Fixed pixel sizing
        html.Div([
            html.H2("Fixed-size Gauge", style={'textAlign': 'center'}),
            html.P("Width: 300px, Height: 300px", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="fixed-gauge",
                min_value=0,
                max_value=100,
                value=50,
                width="300px",  # Fixed width
                height="300px", # Fixed height
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),
    
    html.Div([
        # Test 3: Viewport-relative sizing
        html.Div([
            html.H2("Viewport-relative Gauge", style={'textAlign': 'center'}),
            html.P("Width: 40vw, Height: 40vh", style={'textAlign': 'center'}),
            gauge.Gauge(
                id="viewport-gauge",
                min_value=0,
                max_value=100,
                value=60,
                width="40vw",  # 40% of viewport width
                height="40vh", # 40% of viewport height
                gauge_thickness=0.1
            ),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
        
        # Test 4: Container-relative sizing
        html.Div([
            html.H2("Container-relative Gauge", style={'textAlign': 'center'}),
            html.P("Width: 100%, Height: 100%", style={'textAlign': 'center'}),
            html.Div([
                gauge.Gauge(
                    id="container-gauge",
                    min_value=0,
                    max_value=100,
                    value=85,
                    width="100%",  # 100% of container width
                    height="100%", # 100% of container height
                    gauge_thickness=0.1
                ),
            ], style={'width': '100%', 'height': '300px', 'border': '1px solid #ddd'}),
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'}),
    ]),
    
    # Dynamic value gauge to test text scaling
    html.Div([
        html.H2("Dynamic Value Gauge", style={'textAlign': 'center'}),
        html.P("The value updates every second to test text scaling", style={'textAlign': 'center'}),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
        ),
        gauge.Gauge(
            id="dynamic-gauge",
            min_value=0,
            max_value=100,
            value=0,
            width="100%",
            height="300px",
            gauge_thickness=0.1
        ),
    ], style={'width': '90%', 'margin': '0 auto', 'padding': '10px'}),
])

# Callback to update the dynamic gauge value
@app.callback(
    Output('dynamic-gauge', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_gauge(n):
    # Value cycles between 0 and 100
    return n % 101

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8057)