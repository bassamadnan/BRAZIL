from xml.etree import ElementTree as ET
from app.shapes.group import Group


def import_xml_to_list(element, data_list=None):
    if data_list is None:
        data_list = []

    for child in element:
        if child.tag == 'group':
            group_data = {'type': 'group', 'objects': []}
            data_list.append(group_data)
            import_xml_to_list(child, group_data['objects'])
        elif child.tag == 'rectangle':
            upper_left = child.find('upper-left')
            lower_right = child.find('lower-right')
            color = child.find('color').text
            corner = child.find('corner').text

            data_list.append({
                'type': 'rectangle',
                'upper_left': {
                    'x': int(upper_left.find('x').text),
                    'y': int(upper_left.find('y').text)
                },
                'lower_right': {
                    'x': int(lower_right.find('x').text),
                    'y': int(lower_right.find('y').text)
                },
                'color': color,
                'corner': corner
            })
        elif child.tag == 'line':
            begin = child.find('begin')
            end = child.find('end')
            color = child.find('color').text

            data_list.append({
                'type': 'line',
                'begin': {
                    'x': int(begin.find('x').text),
                    'y': int(begin.find('y').text)
                },
                'end': {
                    'x': int(end.find('x').text),
                    'y': int(end.find('y').text)
                },
                'color': color
            })

    return data_list