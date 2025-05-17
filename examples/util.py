class Util:
    def __init__(self):
        raise ValueError("Cannot instantiate this Util class")

    @classmethod
    def generate_gradient_colors(cls, start_color, end_color, steps, begin_value, end_value):
        """
        Generate a gradient of colors with evenly divided value ranges.

        Args:
            start_color (str): The starting color in hex format (e.g., '#FF0000').
            end_color (str): The ending color in hex format (e.g., '#00FF00').
            steps (int): Total number of gradient steps.
            begin_value (float): The start value of the range.
            end_value (float): The end value of the range.

        Returns:
            List[dict]: A list of dictionaries, each containing 'min', 'max', and 'color'.
                        Example: {'min': 0, 'max': 25, 'color': '#FF0000'}.
        """

        # Helper functions to convert between hex and RGB
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        def rgb_to_hex(rgb_color):
            return "#{:02x}{:02x}{:02x}".format(*rgb_color)

        # Convert start and end colors to RGB
        start_rgb = hex_to_rgb(start_color)
        end_rgb = hex_to_rgb(end_color)

        # Calculate step sizes for R, G, B channels
        step_sizes = [
            (end_rgb[i] - start_rgb[i]) / (steps - 1) for i in range(3)
        ]

        # Calculate range span and step size for values
        value_step = (end_value - begin_value) / steps

        # Generate colors and corresponding value ranges
        gradient_ranges = []
        for i in range(steps):
            # Interpolate RGB values
            color = rgb_to_hex((
                int(start_rgb[0] + step_sizes[0] * i),
                int(start_rgb[1] + step_sizes[1] * i),
                int(start_rgb[2] + step_sizes[2] * i)
            ))

            # Create gradient dict
            gradient_ranges.append({
                "min": begin_value + i * value_step,
                "max": begin_value + (i + 1) * value_step,
                "color": color
            })

        return gradient_ranges
