def lighten_color(hex_color, factor=0.2):
    # Ensure the hex color is in the format '#RRGGBB'
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color format")

    # Convert hex to RGB
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    # Adjust each RGB component
    lighter_rgb = tuple(int(min(255, c + factor * (255 - c))) for c in rgb)

    # Convert RGB to hex
    hex_lighter_color = "#{:02X}{:02X}{:02X}".format(*lighter_rgb)

    return hex_lighter_color


if __name__ == "__main__":
    # Example usage:
    original_color = "#009688"
    lighter_color = lighten_color(original_color)
    print(f"Original color: {original_color}")
    print(f"Lighter color: {lighter_color}")
