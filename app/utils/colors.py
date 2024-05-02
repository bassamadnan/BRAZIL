def get_color_name(color):
    map = {
        "#000000": "black",
        "#ff0000": "red",
        "#008000": "green",
        "#0000ff": "blue"
    }
    if color in map:
        return map[color]
    return color
