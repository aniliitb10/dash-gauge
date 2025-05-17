import unittest
from dash import html
from dash_gauge_component.gauge import Gauge

class TestGauge(unittest.TestCase):
    """Test cases for the Gauge component."""

    def test_initialization(self):
        """Test that the Gauge component initializes correctly with default values."""
        gauge = Gauge(id="test-gauge", value=50)

        # Check that the component is a Div
        self.assertIsInstance(gauge, html.Div)

        # Check that the ID is set correctly
        self.assertEqual(gauge.id, "test-gauge")

        # Check that the value is set correctly
        self.assertEqual(gauge.value, 50)

        # Check default values
        self.assertEqual(gauge.min_value, 0)
        self.assertEqual(gauge.max_value, 100)
        self.assertEqual(gauge.width, '100%')
        self.assertEqual(gauge.height, '100%')
        self.assertEqual(gauge.needle_color, '#000000')
        self.assertEqual(gauge.needle_thickness, 8.0)
        self.assertEqual(gauge.show_value, True)
        self.assertEqual(gauge.start_angle, 225)
        self.assertEqual(gauge.end_angle, -45)
        self.assertEqual(gauge.gauge_thickness, 0.1)

    def test_custom_values(self):
        """Test that the Gauge component accepts custom values."""
        gauge = Gauge(
            id="custom-gauge",
            value=75,
            min_value=25,
            max_value=125,
            width='50%',
            height='300px',
            color_ranges=[
                {'min': 25, 'max': 75, 'color': '#FF0000'},
                {'min': 75, 'max': 125, 'color': '#00FF00'},
            ],
            needle_color='#0000FF',
            needle_thickness=3.0,
            show_value=False,
            start_angle=-90,
            end_angle=90,
            gauge_thickness=0.2,
        )

        # Check that custom values are set correctly
        self.assertEqual(gauge.id, "custom-gauge")
        self.assertEqual(gauge.value, 75)
        self.assertEqual(gauge.min_value, 25)
        self.assertEqual(gauge.max_value, 125)
        self.assertEqual(gauge.width, '50%')
        self.assertEqual(gauge.height, '300px')
        self.assertEqual(len(gauge.color_ranges), 2)
        self.assertEqual(gauge.color_ranges[0]['min'], 25)
        self.assertEqual(gauge.color_ranges[0]['max'], 75)
        self.assertEqual(gauge.color_ranges[0]['color'], '#FF0000')
        self.assertEqual(gauge.color_ranges[1]['min'], 75)
        self.assertEqual(gauge.color_ranges[1]['max'], 125)
        self.assertEqual(gauge.color_ranges[1]['color'], '#00FF00')
        self.assertEqual(gauge.needle_color, '#0000FF')
        self.assertEqual(gauge.needle_thickness, 3.0)
        self.assertEqual(gauge.show_value, False)
        self.assertEqual(gauge.start_angle, -90)
        self.assertEqual(gauge.end_angle, 90)
        self.assertEqual(gauge.gauge_thickness, 0.2)

    def test_children(self):
        """Test that the Gauge component has the correct children."""
        gauge = Gauge(id="test-gauge", value=50)

        # Check that the component has one child (the Graph)
        self.assertEqual(len(gauge.children), 1)

        # Check that the child is a Graph
        from dash import dcc
        self.assertIsInstance(gauge.children[0], dcc.Graph)

        # Check that the Graph has the correct ID
        self.assertEqual(gauge.children[0].id, "test-gauge-graph")


if __name__ == '__main__':
    unittest.main()
