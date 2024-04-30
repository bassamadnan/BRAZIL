from PyQt5.QtCore import QRectF

class Group:
    def __init__(self, objects=None):
        self.objects = objects or []

    def boundingRect(self):
        if not self.objects:
            return QRectF()
        
        rects = [obj.boundingRect() for obj in self.objects]
        x1 = min(rect.x() for rect in rects)
        y1 = min(rect.y() for rect in rects)
        x2 = max(rect.x() + rect.width() for rect in rects)
        y2 = max(rect.y() + rect.height() for rect in rects)
        return QRectF(x1, y1, x2 - x1, y2 - y1)

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)
