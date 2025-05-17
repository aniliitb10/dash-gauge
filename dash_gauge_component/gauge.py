import numpy as np
import plotly.graph_objects as go
from dash import html, dcc


class Gauge(html.Div):
    """
    A responsive gauge component for Dash applications.

    This component creates a gauge chart with a needle that points to a value.
    The gauge is fully responsive and can be customized with various options.

    Parameters
    ----------
    id : str
        The ID of this component, used to identify dash components in callbacks
    value : float
        The value to display on the gauge
    min_value : float, optional
        The minimum value of the gauge (default 0)
    max_value : float, optional
        The maximum value of the gauge (default 100)
    width : str, optional
        The width of the gauge as a percentage of the container (default '100%')
    height : str, optional
        The height of the gauge as a percentage of the container (default '100%')
    color_ranges : list of dict, optional
        A list of dictionaries defining color ranges for the gauge
        Each dict should have 'min', 'max', and 'color' keys
        Example: [{'min': 0, 'max': 50, 'color': '#FF0000'}, {'min': 50, 'max': 100, 'color': '#00FF00'}]
    needle_color : str, optional
        The color of the needle (default '#000000')
    needle_thickness : float, optional
        The thickness of the needle as a percentage of the gauge radius (default 2.0)
    show_value : bool, optional
        Whether to display the value as text (default True)
    start_angle : float, optional
        The starting angle of the gauge in degrees (default 225, bottom left)
    end_angle : float, optional
        The ending angle of the gauge in degrees (default -45, bottom right)
    gauge_thickness : float, optional
        The thickness of the gauge arc as a fraction of the radius (default 0.1)
    value_format : str, optional
        Format string for the displayed value (default "{:.1f}")
        Examples: "{:.0f}" for no decimal places, "{:.1f}%" for percentage with 1 decimal place
    value_font_family : str, optional
        Font family for the value text (default "Arial, sans-serif")
    value_font_size : int, optional
        Base font size for the value text (default 16)
    value_font_weight : str, optional
        font weight for the value text (default "bold")
    value_font_color : str, optional
        Color for the value text (default "rgba(0,0,0,0.8)"), use "auto" to match the color of pointed value
    tick_font_size : int, optional
        Font size for the tick labels (default 10)
    tick_font_color : str, optional
        Color for the tick labels (default "rgba(0,0,0,0.7)")
    tick_label_radius : float, optional
        Shows the distance from the center of the gauge to the tick labels as a fraction of the radius (default 1.1)
    """

    def __init__(
            self,
            id,
            value,
            min_value=0,
            max_value=100,
            width='100%',
            height='100%',
            color_ranges=None,
            needle_color='#000000',
            needle_thickness=8.0,
            show_value=True,
            start_angle=225,  # Start from the bottom left (225 degrees)
            end_angle=-45,  # End at bottom right (-45 degrees)
            gauge_thickness=0.1,  # Thickness of the gauge arc as a fraction of the radius

            value_format="{:.1f}",  # Format string for the displayed value
            value_font_family="Arial, sans-serif",  # Font family for the value text
            value_font_size=16,  # Base font size for the value text
            value_font_color="rgba(0,0,0,0.8)",  # Color for the value text
            value_font_weight='bold',

            tick_font_size=10,  # Font size for the tick labels
            tick_font_color="rgba(0,0,0,0.7)",  # Color for the tick labels
            tick_label_radius=1.1,
            **kwargs
    ):
        self.id = id
        self.min_value = min_value
        self.max_value = max_value
        self._value = self._validate_value(value)
        self.width = width
        self.height = height
        self.color_ranges = color_ranges or [
            {'min': min_value, 'max': max_value, 'color': '#1f77b4'}
        ]
        self.needle_color = needle_color
        self.needle_thickness = needle_thickness
        self.show_value = show_value
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.gauge_thickness = gauge_thickness

        self.value_format = value_format
        self.value_font_family = value_font_family
        self.value_font_size = value_font_size
        self.value_font_color = value_font_color
        self.value_font_weight = value_font_weight

        self.tick_font_size = tick_font_size
        self.tick_font_color = tick_font_color
        self.tick_label_radius = tick_label_radius

        # Create the gauge figure
        fig = self._create_gauge_figure()

        # Create a responsive container for the gauge
        super().__init__(
            id=id,
            children=[
                dcc.Graph(
                    id=f"{id}-graph",
                    figure=fig,
                    config={
                        'displayModeBar': False,
                        'responsive': True,  # Ensure the graph is responsive
                    },
                    style={
                        'width': width,
                        'height': height,
                        'min-width': '100px',  # Minimum width to prevent too small rendering
                        'min-height': '100px',  # Minimum height to prevent too small rendering
                    },
                    responsive=True,
                )
            ],
            style={
                'width': width,
                'height': height,
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'overflow': 'visible',  # Allow content to expand beyond container
            },
            **kwargs
        )

    def _validate_value(self, value):
        """Validate and clamp the value to be within min_value and max_value."""
        if value < self.min_value:
            return self.min_value
        elif value > self.max_value:
            return self.max_value
        return value

    @property
    def value(self):
        """Get the current value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Set the value, ensuring it's within the valid range."""
        self._value = self._validate_value(new_value)

    def _create_gauge_figure(self):
        """Create the gauge figure using Plotly."""
        # Convert angles from degrees to radians
        start_angle_rad = np.radians(self.start_angle)
        end_angle_rad = np.radians(self.end_angle)

        # Calculate the angle for the current value
        value_normalized = (self.value - self.min_value) / (self.max_value - self.min_value)
        value_angle_rad = start_angle_rad + value_normalized * (end_angle_rad - start_angle_rad)

        # Create the base figure
        fig = go.Figure()

        # Add a background circle for better aesthetics - use more points for smoother circle
        theta_circle = np.linspace(0, 2 * np.pi, 500)  # Increased from 300 to 500 points for smoother circle
        x_circle = 0.85 * np.cos(theta_circle)
        y_circle = 0.85 * np.sin(theta_circle)

        fig.add_trace(go.Scatter(
            x=x_circle.tolist(),
            y=y_circle.tolist(),
            mode='lines',
            line=dict(
                color='rgba(200,200,200,0.2)',
                width=1,
            ),
            fill='toself',
            fillcolor='rgba(200,200,200,0.1)',
            hoverinfo='skip',
            showlegend=False,
        ))

        # Add the gauge background as arcs (not filled)
        for color_range in self.color_ranges:
            min_val = color_range['min']
            max_val = color_range['max']
            color = color_range['color']

            # Normalize the range
            min_norm = (min_val - self.min_value) / (self.max_value - self.min_value)
            max_norm = (max_val - self.min_value) / (self.max_value - self.min_value)

            # Calculate angles for this range
            min_angle = start_angle_rad + min_norm * (end_angle_rad - start_angle_rad)
            max_angle = start_angle_rad + max_norm * (end_angle_rad - start_angle_rad)

            # Create points for the arc - use more points for smoother curve
            theta = np.linspace(min_angle, max_angle,
                                1000)  # Increased from 300 to 1000 points for extremely smooth curve
            r = np.ones_like(theta)

            # Convert to cartesian coordinates
            x = r * np.cos(theta)
            y = r * np.sin(theta)

            # Add the arc for this range
            fig.add_trace(go.Scatter(
                x=x.tolist(),
                y=y.tolist(),
                mode='lines',
                line=dict(
                    color=color,
                    width=self.gauge_thickness * 30,  # Thicker line to represent the gauge arc
                    shape='spline',  # Use spline interpolation for smoother curves
                    smoothing=1.3,  # Increase the smoothing factor for even smoother curves
                ),
                hoverinfo='skip',
                showlegend=False,
            ))

        # Add major tick marks and labels
        num_major_ticks = 6
        major_tick_values = np.linspace(self.min_value, self.max_value, num_major_ticks)
        major_tick_angles = np.linspace(start_angle_rad, end_angle_rad, num_major_ticks)

        # Add minor tick marks
        num_minor_ticks = 5  # Number of minor ticks between major ticks
        for i in range(num_major_ticks - 1):
            # Calculate angles for minor ticks between major ticks
            minor_angles = np.linspace(major_tick_angles[i], major_tick_angles[i + 1], num_minor_ticks + 2)[1:-1]

            # Add minor tick marks
            for angle in minor_angles:
                # Outer radius for minor ticks
                r_outer_minor = 1.0
                # Inner radius for minor ticks
                r_inner_minor = 0.95

                x_tick = [r_inner_minor * np.cos(angle), r_outer_minor * np.cos(angle)]
                y_tick = [r_inner_minor * np.sin(angle), r_outer_minor * np.sin(angle)]

                fig.add_trace(go.Scatter(
                    x=x_tick,
                    y=y_tick,
                    mode='lines',
                    line=dict(
                        color='rgba(0,0,0,0.3)',
                        width=1,
                    ),
                    hoverinfo='skip',
                    showlegend=False,
                ))

        # Outer radius for major ticks
        r_outer = 1.0
        # Inner radius for major ticks
        r_inner = 0.9

        # Add major tick marks and labels
        for i, angle in enumerate(major_tick_angles):
            x_tick = [r_inner * np.cos(angle), r_outer * np.cos(angle)]
            y_tick = [r_inner * np.sin(angle), r_outer * np.sin(angle)]

            fig.add_trace(go.Scatter(
                x=x_tick,
                y=y_tick,
                mode='lines',
                line=dict(
                    color='rgba(0,0,0,0.7)',
                    width=2,
                ),
                hoverinfo='skip',
                showlegend=False,
            ))

            # Add tick labels
            fig.add_annotation(
                x=self.tick_label_radius * np.cos(angle),
                y=self.tick_label_radius * np.sin(angle),
                text=f"{major_tick_values[i]:.0f}",
                showarrow=False,
                font=dict(
                    size=self.tick_font_size,
                    color=self.tick_font_color,
                    family=self.value_font_family
                ),
            )

        # Add the needle with a triangular shape
        needle_length = 0.85  # Length of the needle as a fraction of the gauge radius
        needle_width = self.needle_thickness * 0.02  # Width of the needle base

        # Calculate needle points for a triangular shape
        needle_tip_x = needle_length * np.cos(value_angle_rad)
        needle_tip_y = needle_length * np.sin(value_angle_rad)

        # Calculate the perpendicular angle for the base of the needle
        perp_angle = value_angle_rad + np.pi / 2

        # Calculate base points of the needle
        base_x1 = needle_width * np.cos(perp_angle)
        base_y1 = needle_width * np.sin(perp_angle)
        base_x2 = -needle_width * np.cos(perp_angle)
        base_y2 = -needle_width * np.sin(perp_angle)

        # Create the needle shape
        x_needle = [base_x1, needle_tip_x, base_x2, base_x1]
        y_needle = [base_y1, needle_tip_y, base_y2, base_y1]

        # Add the needle
        fig.add_trace(go.Scatter(
            x=x_needle,
            y=y_needle,
            mode='lines',
            line=dict(
                color=self.needle_color,
                width=1,
            ),
            fill='toself',
            fillcolor=self.needle_color,
            hoverinfo='skip',
            showlegend=False,
        ))

        # Add a center dot for the needle
        fig.add_trace(go.Scatter(
            x=[0],
            y=[0],
            mode='markers',
            marker=dict(
                color=self.needle_color,
                size=self.needle_thickness * 5,  # Multiply by 5 for better visibility
                line=dict(
                    color='rgba(255,255,255,0.8)',
                    width=1,
                ),
            ),
            hoverinfo='skip',
            showlegend=False,
        ))

        # Add the value text if requested
        if self.show_value:
            # Use a responsive font size that scales with the gauge
            # This ensures the text is always proportional to the gauge size
            # Format the value using the provided format string
            formatted_value = self.value_format.format(self.value)
            if self.value_font_color == "auto":
                for color_data in self.color_ranges:
                    if color_data['min'] <= self.value <= color_data['max']:
                        self.value_font_color = color_data['color']
                        break

                # if still couldn't find the color, then, raise an exception
                if self.value_font_color == "auto":
                    raise ValueError("value_font_color must be specified if value is outside of color_ranges")

            fig.add_annotation(
                x=0,
                y=-0.6,  # Position further below the gauge to avoid overlap with the center dot
                text=formatted_value,
                showarrow=False,
                font=dict(
                    size=self.value_font_size,  # Base size that will be scaled by the container
                    color=self.value_font_color,  # Use the provided font color
                    family=self.value_font_family,  # Use the provided font family
                    weight=self.value_font_weight,
                ),
                xanchor='center',
                yanchor='middle',
            )

        # Configure the layout for a clean gauge appearance
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                range=[-1.3, 1.3],  # Slightly larger range to accommodate labels
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                fixedrange=True,
                scaleanchor="y",  # This ensures x and y have the same scale
                scaleratio=1,  # 1:1 aspect ratio
                constrain='domain',  # Constrain the axis to maintain aspect ratio
            ),
            yaxis=dict(
                range=[-1.3, 1.3],  # Slightly larger range to accommodate labels
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                fixedrange=True,
                constrain='domain',  # Constrain the axis to maintain aspect ratio
            ),
            autosize=True,  # Allow the figure to be resized automatically
            width=None,  # Let the container determine the width
            height=None,  # Let the container determine the height
            uirevision='true',  # Maintain state when resizing
        )

        return fig
