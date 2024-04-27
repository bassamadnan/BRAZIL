from PyQt5.QtCore import QRectF

def get_line_bounding_rect(line):
    x1 = min(line.start_point.x(), line.end_point.x())
    y1 = min(line.start_point.y(), line.end_point.y())
    x2 = max(line.start_point.x(), line.end_point.x())
    y2 = max(line.start_point.y(), line.end_point.y())
    return QRectF(x1, y1, x2 - x1, y2 - y1)

def contains_line(line, pos):
    line_rect = get_line_bounding_rect(line)
    return line_rect.contains(pos)