def indent_xml(xml_str, level=0):
    indent_str = ' ' * 4 * level + xml_str + '\n'
    return indent_str

def nest(xml_str, indent):
    parsed = xml_str.split("\n")
    for i in range(len(parsed)):
        parsed[i] = 4*indent + parsed[i]
    return '\n'.join(parsed)