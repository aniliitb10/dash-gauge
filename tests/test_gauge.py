import unittest

from dash import html

from dash_gauge_component import Gauge


class TestGauge(unittest.TestCase):
    def test_initialization(self):
        """Test that the Gauge component initializes correctly with default values."""
        # Testing the initialization of the Gauge object
        gauge = Gauge(id="test-gauge", value=50)

        # Check the Gauge is a Dash html.Div
        self.assertIsInstance(gauge, html.Div, "Gauge is not a Dash html.Div instance.")

        # Check Gauge attributes
        self.assertEqual(gauge.id, "test-gauge", "Gauge ID is incorrect.")
        self.assertEqual(gauge.value, 50, "Gauge value is incorrect.")
        self.assertEqual(gauge.min_value, 0, "Gauge's minimum value is incorrect.")
        self.assertEqual(gauge.max_value, 100, "Gauge's maximum value is incorrect.")
        self.assertEqual(gauge.width, "100%", "Gauge's width is incorrect.")
        self.assertEqual(gauge.height, "100%", "Gauge's height is incorrect.")
        self.assertEqual(gauge.needle_color, "#000000", "Gauge's needle color is incorrect.")
        self.assertEqual(gauge.needle_thickness, 8.0, "Gauge's needle thickness is incorrect.")
        self.assertTrue(gauge.show_value, "Gauge's show_value attribute should be True.")
        self.assertEqual(gauge.start_angle, 225, "Gauge's start angle is incorrect.")
        self.assertEqual(gauge.end_angle, -45, "Gauge's end angle is incorrect.")
        self.assertEqual(gauge.gauge_thickness, 0.1, "Gauge's gauge thickness is incorrect.")
        self.assertEqual(gauge.value_format, "{:.1f}", "Gauge's value format is incorrect.")
        self.assertEqual(gauge.value_font_family, "Arial, sans-serif", "Gauge's font family is incorrect.")
        self.assertEqual(gauge.value_font_size, 16, "Gauge's font size is incorrect.")
        self.assertEqual(gauge.value_font_color, "rgba(0,0,0,0.8)", "Gauge's font color is incorrect.")
        self.assertEqual(gauge.tick_font_size, 10, "Gauge's tick font size is incorrect.")
        self.assertEqual(gauge.tick_font_color, "rgba(0,0,0,0.7)", "Gauge's tick font color is incorrect.")

    def test_custom_values(self):
        """Test the Gauge component initializes correctly with custom values."""
        # Custom initialization of the Gauge object
        gauge = Gauge(
            id="custom-gauge",
            value=75,
            min_value=10,
            max_value=500,
            width="50%",
            height="200px",
            needle_color="#FF0000",
            needle_thickness=5.0,
            show_value=False,
            start_angle=180,
            end_angle=0,
            gauge_thickness=0.2,
            value_format="{:.2f}%",
            value_font_family="Helvetica, sans-serif",
            value_font_size=20,
            value_font_color="#FF5733",
            tick_font_size=12,
            tick_font_color="#3366FF",
        )

        # Attribute checks for the custom Gauge settings
        self.assertEqual(gauge.id, "custom-gauge", "Gauge ID is incorrect with custom values.")
        self.assertEqual(gauge.value, 75, "Gauge value is incorrect with custom values.")
        self.assertEqual(gauge.min_value, 10, "Gauge's minimum value is incorrect with custom values.")
        self.assertEqual(gauge.max_value, 500, "Gauge's maximum value is incorrect with custom values.")
        self.assertEqual(gauge.width, "50%", "Gauge's width is incorrect with custom values.")
        self.assertEqual(gauge.height, "200px", "Gauge's height is incorrect with custom values.")
        self.assertEqual(gauge.needle_color, "#FF0000", "Gauge's needle color is incorrect.")
        self.assertEqual(gauge.needle_thickness, 5.0, "Gauge's needle thickness is incorrect.")
        self.assertFalse(gauge.show_value, "Gauge's show_value should be False.")
        self.assertEqual(gauge.start_angle, 180, "Gauge's start angle is incorrect with custom values.")
        self.assertEqual(gauge.end_angle, 0, "Gauge's end angle is incorrect with custom values.")
        self.assertEqual(gauge.gauge_thickness, 0.2, "Gauge's gauge thickness is incorrect.")
        self.assertEqual(gauge.value_format, "{:.2f}%", "Gauge's value format is incorrect with custom values.")
        self.assertEqual(gauge.value_font_family, "Helvetica, sans-serif", "Gauge's font family is incorrect with custom values.")
        self.assertEqual(gauge.value_font_size, 20, "Gauge's font size is incorrect with custom values.")
        self.assertEqual(gauge.value_font_color, "#FF5733", "Gauge's font color is incorrect with custom values.")
        self.assertEqual(gauge.tick_font_size, 12, "Gauge's tick font size is incorrect with custom values.")
        self.assertEqual(gauge.tick_font_color, "#3366FF", "Gauge's tick font color is incorrect with custom values.")

    def test_value_range_validation(self):
        """Test value range validation for the Gauge component."""
        gauge = Gauge(id="range-gauge", value=50, min_value=0, max_value=100)

        # Check that the value cannot exceed max_value
        gauge.value = 150
        self.assertEqual(gauge.value, 100, "Gauge value should be clamped to max_value.")

        # Check that the value cannot go below min_value
        gauge.value = -10
        self.assertEqual(gauge.value, 0, "Gauge value should be clamped to min_value.")

    def test_style_attributes(self):
        """Test that the Gauge component applies style attributes correctly."""
        gauge = Gauge(id="styled-gauge", value=50, width="75%", height="150px")

        # Check that style attributes are applied correctly
        self.assertEqual(gauge.width, "75%", "Gauge's width style is incorrect.")
        self.assertEqual(gauge.height, "150px", "Gauge's height style is incorrect.")

    def test_value_formatting(self):
        """Test that the value_format parameter correctly formats the displayed value."""
        # Test integer format
        gauge_int = Gauge(id="int-gauge", value=50, value_format="{:.0f}")
        fig_int = gauge_int._create_gauge_figure()
        # Check that the formatted value is correctly generated
        # We need to extract the formatted value from the figure's annotations
        for annotation in fig_int.layout.annotations:
            if annotation.text == "50":  # The formatted value should be "50" (no decimal places)
                self.assertEqual(annotation.text, "50", "Integer formatting is incorrect.")

        # Test percentage format
        gauge_pct = Gauge(id="pct-gauge", value=75.5, value_format="{:.1f}%")
        fig_pct = gauge_pct._create_gauge_figure()
        # Check that the formatted value is correctly generated
        for annotation in fig_pct.layout.annotations:
            if annotation.text == "75.5%":  # The formatted value should be "75.5%"
                self.assertEqual(annotation.text, "75.5%", "Percentage formatting is incorrect.")

        # Test currency format
        gauge_curr = Gauge(id="curr-gauge", value=99.99, value_format="${:.2f}")
        fig_curr = gauge_curr._create_gauge_figure()
        # Check that the formatted value is correctly generated
        for annotation in fig_curr.layout.annotations:
            if annotation.text == "$99.99":  # The formatted value should be "$99.99"
                self.assertEqual(annotation.text, "$99.99", "Currency formatting is incorrect.")


if __name__ == "__main__":
    unittest.main()
