"""Functions for working with color names and hex/rgb values."""

# Primary colors
RED = "#FF0000"
YELLOW = "#FFFF00"
BLUE = "#0000FF"

# Secondary colors
ORANGE = "#FFA500"
GREEN = "#008000"
VIOLET = "#EE82EE"

# Neutral colors
BLACK = "#000000"
GRAY = "#808080"
WHITE = "#FFFFFF"

def _tohex(value):
    """Converts an integer to an 8-bit (2-digit) hexadecimal string."""
    if value <= 0:
        return "00"
    if value >= 255:
        return "FF"
    return format(value, "02X")

def tohex(r, g, b):
    """Formats red, green, and blue integers as a color in hexadecimal."""
    return "#" + _tohex(r) + _tohex(g) + _tohex(b)

def torgb(color):
    """Converts a color in hexadecimal to red, green, and blue integers."""
    r = int(color[1:3], 16) # First 2 digits
    g = int(color[3:5], 16) # Middle 2 digits
    b = int(color[5:7], 16) # Last 2 digits
    return r, g, b

def lighten(color):
    """Increases the red, green, and blue values of a color by 32 each."""
    r, g, b = torgb(color)
    return tohex(r+32, g+32, b+32)

def darken(color):
    """Decreases the red, green, and blue values of a color by 32 each."""
    r, g, b = torgb(color)
    return tohex(r-32, g-32, b-32)
