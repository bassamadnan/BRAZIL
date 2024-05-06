from xml.etree import ElementTree as ET
from app.shapes.group import Group


def import_xml_to_list(file_path):
    """
    Just take the int value to avoid precision errors for the cordinates.
    """
    data_list = []
    tree = ET.parse(file_path)
    root = tree.getroot()

    # iterate over the elements and extract data
    for element in root:
        if element.tag == 'group':
            group = Group()
            data_list.append({'type': 'group', 'objects': []})
            for child in element:
                if child.tag == 'rectangle':
                    upper_left = child.find('upper-left')
                    lower_right = child.find('lower-right')
                    color = child.find('color').text
                    corner = child.find('corner').text

                    data_list[-1]['objects'].append({
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

                    data_list[-1]['objects'].append({
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
        elif element.tag == 'rectangle':
            upper_left = element.find('upper-left')
            lower_right = element.find('lower-right')
            color = element.find('color').text
            corner = element.find('corner').text

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
        elif element.tag == 'line':
            begin = element.find('begin')
            end = element.find('end')
            color = element.find('color').text

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
