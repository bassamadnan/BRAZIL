from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt, QPointF
from app.shapes.rectangle import Rectangle
from app.shapes.line import Line
from app.utils.highlight import contains_line
from app.shapes.group import Group

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.groups = []
        self.current_shape = None
        self.selected_shape = None
        self.dragging = False
        self.drag_start_pos = None
        self.shape_start_pos = None
        self.selected_shapes = set()
        self.selected_groups = set()

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
            if self.selected_shape == shape:
                self.selected_shape = None
        # print(self.shapes)

    def select_shape(self, pos):
        for group in self.groups:
            if group.boundingRect().contains(pos):
                self.selected_shape = group
                self.dragging = True
                self.drag_start_pos = pos
                self.shape_start_pos = QPointF(group.boundingRect().topLeft())
                return

        for shape in self.shapes:
            if isinstance(shape, Rectangle) and shape.boundingRect().contains(pos):
                self.selected_shape = shape
                self.dragging = True
                self.drag_start_pos = pos
                self.shape_start_pos = QPointF(self.selected_shape.start_point)
                return
            elif isinstance(shape, Line):
                if contains_line(shape, pos):
                    self.selected_shape = shape
                    self.dragging = True
                    self.drag_start_pos = pos
                    self.shape_start_pos = QPointF(self.selected_shape.start_point)
                    return
        self.selected_shape = None
        self.dragging = False

    def update_shape_position(self, pos):
        if self.dragging:
            delta = pos - self.drag_start_pos
            if isinstance(self.selected_shape, Group):
                self.update_group_position(self.selected_shape, delta)
            elif isinstance(self.selected_shape, Rectangle):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            elif isinstance(self.selected_shape, Line):
                self.selected_shape.start_point += delta
                self.selected_shape.end_point += delta
            self.drag_start_pos = pos

    def update_group_position(self, group, delta):
        for obj in group.objects:
            if isinstance(obj, Group):
                self.update_group_position(obj, delta)
            elif isinstance(obj, Rectangle):
                obj.start_point += delta
                obj.end_point += delta
            elif isinstance(obj, Line):
                obj.start_point += delta
                obj.end_point += delta

    def draw_shapes(self, painter):
        for group in self.groups:
            group_rect = group.boundingRect()
            painter.setPen(QPen(Qt.black, 1, Qt.DotLine))  # Set dotted thin line pen
            painter.drawRect(group_rect)

            # Draw individual shapes within the group
            for shape in group.objects:
                if isinstance(shape, Line):
                    painter.setPen(QPen(shape.color, 3))
                    painter.drawLine(shape.start_point, shape.end_point)
                elif isinstance(shape, Rectangle):
                    shape_rect = shape.boundingRect()
                    painter.setPen(QPen(shape.color, 3))
                    if shape.rounded:
                        painter.drawRoundedRect(shape_rect, 10, 10)
                    else:
                        painter.drawRect(shape_rect)

            # Highlight the selected group
            if group in self.selected_shapes:
                painter.setPen(QPen(Qt.yellow, 1, Qt.DotLine))  # Set yellow dotted thin line pen
                painter.drawRect(group_rect)
            
        for shape in self.shapes:
            if isinstance(shape, Line):
                painter.setPen(QPen(shape.color, 3))
                painter.drawLine(shape.start_point, shape.end_point)

                # Highlight the selected lines
                if shape in self.selected_shapes or shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 5))
                    painter.drawLine(shape.start_point, shape.end_point)
            elif isinstance(shape, Rectangle):
                shape_rect = shape.boundingRect()
                painter.setPen(QPen(shape.color, 3))
                if shape.rounded:
                    painter.drawRoundedRect(shape_rect, 10, 10)
                else:
                    painter.drawRect(shape_rect)

                # Highlight the selected rectangles
                if shape in self.selected_shapes or shape is self.selected_shape:
                    painter.setPen(QPen(Qt.yellow, 3))
                    if shape.rounded:
                        painter.drawRoundedRect(shape_rect, 10, 10)
                    else:
                        painter.drawRect(shape_rect)

        # Drawing logic
        if self.current_shape:
            if isinstance(self.current_shape, Line):
                painter.setPen(QPen(Qt.black, 3))
                painter.drawLine(self.current_shape.start_point, self.current_shape.end_point)
            elif isinstance(self.current_shape, Rectangle):
                shape_rect = self.current_shape.boundingRect()
                painter.setPen(QPen(Qt.black, 3))
                if self.current_shape.rounded:
                    painter.drawRoundedRect(shape_rect, 10, 10)
                else:
                    painter.drawRect(shape_rect)

    def get_shape_at_pos(self, pos):
        for shape in self.shapes:
            if isinstance(shape, Rectangle) and shape.boundingRect().contains(pos):
                return shape
            elif isinstance(shape, Line):
                if contains_line(shape, pos):
                    return shape
        return None
    
    def toggle_selection(self, obj):
        if isinstance(obj, Group):
            if obj in self.selected_shapes:
                self.selected_shapes.remove(obj)
            else:
                self.selected_shapes.add(obj)
        else:
            if obj in self.selected_shapes:
                self.selected_shapes.remove(obj)
            else:
                self.selected_shapes.add(obj)

    def create_group(self):
        group_shapes = list(self.selected_shapes)
        group_groups = list(self.selected_groups)
        print(group_shapes)
        print(group_groups)
        if group_shapes or group_groups:
            group = Group()
            for shape in group_shapes:
                group.add_object(shape)
            for subgroup in group_groups:
                group.add_object(subgroup)
            self.groups.append(group)
            self.selected_shapes.clear()
            self.selected_groups.clear()
            self.toggle_selection(group)
    
    def ungroup(self, group):
        if group in self.groups:
            self.groups.remove(group)
            for obj in group.objects:
                if isinstance(obj, Group):
                    if obj not in self.groups:
                        self.groups.append(obj)
                else:
                    if obj not in self.shapes:
                        self.shapes.append(obj)
            if self.selected_shape == group:
                self.selected_shape = None
    
    def remove_group(self, group):
        if group in self.groups:
            self.groups.remove(group)
            self.remove_group_objects(group)
            if self.selected_shape == group:
                self.selected_shape = None
                
    def remove_group_objects(self, group):
        for obj in group.objects:
            if isinstance(obj, Group):
                self.remove_group_objects(obj)
                if obj in self.groups:
                    self.groups.remove(obj)
            elif obj in self.shapes:
                self.shapes.remove(obj)
    
   
    def add_group(self, group):
        self.groups.append(group)
        self.add_group_objects(group)

    def add_group_objects(self, group):
        for obj in group.objects:
            if isinstance(obj, Group):
                self.add_group_objects(obj)
            else:
                if obj not in self.shapes:
                    self.shapes.append(obj)
    
    def export_shapes(self):
        xml = ''
        for shape in self.shapes:
            xml += shape.export()
        return xml
