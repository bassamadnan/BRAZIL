from PyQt5.QtCore import QRectF
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line


class Group:
    """
    Group class for handling the data structure
    """
    def __init__(self, objects=None):
        self.objects = objects or []
        self.belonging_group = None
    
    def boundingRect(self):
        if not self.objects:
            return QRectF()

        x_coords = []
        y_coords = []

        for obj in self.objects:
            if isinstance(obj, Group):
                rect = obj.boundingRect()
            elif isinstance(obj, Rectangle):
                rect = obj.boundingRect()
            elif isinstance(obj, Line):
                x_coords.extend([obj.start_point.x(), obj.end_point.x()])
                y_coords.extend([obj.start_point.y(), obj.end_point.y()])
                continue

            x_coords.extend([rect.x(), rect.x() + rect.width()])
            y_coords.extend([rect.y(), rect.y() + rect.height()])

        if not x_coords or not y_coords:
            return QRectF()

        x1 = min(x_coords)
        y1 = min(y_coords)
        x2 = max(x_coords)
        y2 = max(y_coords)

        return QRectF(x1, y1, x2 - x1, y2 - y1)

    def add_object(self, obj):
        self.objects.append(obj)
        obj.belonging_group = self


    def remove_object(self, obj):
        self.objects.remove(obj)
        obj.belonging_group = None
