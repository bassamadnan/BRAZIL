import math

def closest_point(x1, y1, x2, y2, x, y):
    if x1 == x2:
        return (x1,y)
    if y1 == y2:
        return (x,y1)
    m1 = (y2 - y1) / (x2 - x1)
    m2 = -1 / m1
    x_c = (m1 * x1 - m2 * x + y - y1) / (m1 - m2)
    y_c = m2 * (x_c - x) + y
    return (x_c, y_c)

def distance_from_edge(x1, y1, x2, y2, x, y):
    x_c, y_c = closest_point(x1, y1, x2, y2, x, y)
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)
    x_bound = x_min <= x_c and x_c <= x_max
    y_bound = y_min <= y_c and y_c <= y_max
    if x_bound and y_bound:
        return math.sqrt((x - x_c)**2 + (y - y_c)**2)
    return 1e30
