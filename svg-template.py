style = 'stroke="black" stroke-width="1px"'

def draw_svg(width, height, shapes):
    """Puts svg header and footer around some svg shapes.
    Input:
    - width: int, desired width of the svg drawing in pixels
    - height: int, desired height of the svg drawing in pixels
    - shapes: str, svg code describing the contents of the drawing
    Output:
    - str, the given svg code surrounded by header and footer tags
    """
    viewbox = 'viewBox="0 0 ' + str(width) + ' ' + str(height) + '"'
    xmlns = 'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
    header = '<svg width="' + str(width) + '" height="' + str(height) + '" ' + xmlns + viewbox +  '>'
    footer = '</svg>'
    return header + shapes + footer

def save(svg, filename):
    """Saves some svg code to a file.
    Input:
    - svg: str, the svg code (made with draw_svg)
    - filename: str, name of the file to save in
    """
    with open(filename, 'w') as f:
        f.write(svg)

def draw_circle(x, y, radius, color):
    """Creates svg code for drawing a circle.
    Input:
    - x: int, x-coordinate of the center of the circle in pixels
    - y: int, y-coordinate of the center of the circle in pixels
    - radius: int, radius of the circle in pixels
    - color: str, color of the circle in hex
    Output:
    - str, svg code describing a circle
    """
    cx = 'cx="' + str(x) + '"'
    cy = 'cy="' + str(y) + '"'
    rad = 'r="' + str(radius) + '"'
    return '<circle ' + cx + ' ' + cy + ' ' + rad + ' ' + 'fill="' + color + '" ' + style + '/>'


def draw_rect(x, y, width, height, color):
    """Creates SVG-code for drawing a rectangle.
    Input:
    - x: int, x-coordinate for left corner in pixels
    - y: int, y-coordinate for left corner in pixels
    - width: int, width of the rectangle in pixels
    - height: int, height of the rectangle in pixels
    - color: str, color of the rectangle in hex
    Output:
    - str, SVG-code describing a rectangle
    """
    rx = 'x="' + str(x) + '"'
    ry = 'y="'+ str(y) + '"'
    rw = 'width="' + str(width) + '"'
    rh = 'height="' + str(height) + '"'
    return '<rect ' + rx + ' ' + ry + ' ' + rw + ' ' + rh + ' ' + 'fill="' + color + '" ' + style + '/>'


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    """Creates SVG-code for drawing a rectangle.
        Input:
        - x1: int, x-coordinate for first corner in pixels
        - y1: int, y-coordinate for first corner in pixels
        - x2: int, x-coordinate for second corner in pixels
        - y2: int, y-coordinate for second corner in pixels
        - x3: int, x-coordinate for third corner in pixels
        - y3: int, y-coordinate for third corner in pixels
        - color: str, color of the triangle in hex
        Output:
        - str, SVG-code describing a triangle
        """
    point1 = str(x1) + ',' + str(y1)
    point2 = str(x2) + ',' + str(y2)
    point3 = str(x3) + ',' + str(y3)
    return '<polygon points="' + point1 + ' ' + point2 + ' ' + point3 + '" ' + 'fill="' + color + '" ' + style + '/>'


# My snowman:
"""Setting the screen-size"""
width, height = 500, 500
center = width/2

"""Drawing the shapes"""
snowman = ""
snowman += draw_rect(0, 0, width, height, '#ffffff')

for i in range(3):
    snowman += draw_circle(center, 410 - (80*i), 90 - (20*i), '#ffffff')
    snowman += draw_circle(center, 410 - (45*i), 5, '#000000')

snowman += draw_rect(215, 130, 70, 80, '#000000')
snowman += draw_rect(200, 210, 100, 5, '#000000')
snowman += draw_triangle(240, 260, 260, 260, 250, 290, '#ffa500')


# Turn the shapes into a proper SVG drawing, on a 500x500 canvas
drawing = draw_svg(width, height, snowman)

# Save the example drawing to a file
save(drawing, 'test.svg')
