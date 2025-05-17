import pytest
import os
import plotly.io as pio
from dash_gauge_component.gauge import Gauge

def test_static_gauge_image_creation():
    """Test that the Gauge component can create a static image."""
    # Create a gauge instance
    gauge_instance = Gauge(
        id="test-gauge",
        value=75,
        min_value=0,
        max_value=100,
        width="100%",
        height="600px",
        color_ranges=[
            {'min': 0, 'max': 25, 'color': '#FF0000'},  # Red
            {'min': 25, 'max': 75, 'color': '#FFFF00'},  # Yellow
            {'min': 75, 'max': 100, 'color': '#00FF00'},  # Green
        ],
        needle_color="#000000",
        needle_thickness=3.0,
        show_value=True,
        start_angle=-150,
        end_angle=150,
        gauge_thickness=0.1,
    )

    # Get the figure from the gauge instance
    fig = gauge_instance._create_gauge_figure()

    # Define the output path
    output_path = 'gauge_test.png'

    # Save the figure as an image
    pio.write_image(fig, output_path, scale=2)

    # Check that the image was created
    assert os.path.exists(output_path) is True

    # Clean up - remove the image
    if os.path.exists(output_path):
        os.remove(output_path)
