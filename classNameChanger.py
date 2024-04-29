import xml.etree.ElementTree as ET
import re

import xml.etree.ElementTree as ET
import re


def update_svg_classes_and_styles(svg_file, class_names, filename):
    # Register the SVG namespace
    ET.register_namespace("", "http://www.w3.org/2000/svg")

    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Update class attributes in SVG elements
    for elem in root.iter():
        if 'class' in elem.attrib:
            classes = elem.attrib['class'].split()
            new_classes = [f"{filename}-{cls}" if cls in class_names else cls for cls in classes]
            elem.attrib['class'] = ' '.join(new_classes)
    # Update class names in <style> elements and add debugging
    for style in root.iter():
        css_text = style.text

        if css_text:  # Check if there's any CSS text to modify
            for class_name in class_names:
                pattern = r'\.' + re.escape(class_name) + r'(?!\w)'  # Update regex to capture all relevant cases
                new_class_name = f".{filename}-{class_name}"
                css_text, count = re.subn(pattern, new_class_name, css_text)
            style.text = css_text

    # Write the modified SVG back to a new file
    tree.write(f"{filename}-modified.svg", xml_declaration=True, encoding='utf-8')



# Example usage

filename = 'CoursesImage.svg'
classes = ".cls-1, .cls-2, .cls-3, .cls-4, .cls-5, .cls-6, .cls-7, .cls-8, .cls-9, .cls-10, .cls-11, .cls-12, .cls-13, .cls-14, .cls-15, .cls-16, .cls-17, .cls-18, .cls-19, .cls-20, .cls-21, .cls-22, .cls-23, .cls-24, .cls-25, .cls-26, .cls-27, .cls-28, .cls-29, .cls-30, .cls-31, .cls-32, .cls-33, .cls-34, .cls-35, .cls-36, .cls-37, .cls-38, .cls-39, .cls-40, .cls-41, .cls-42, .cls-43, .cls-44, .cls-45, .cls-46, .cls-47, .cls-48, .cls-49, .cls-50, .cls-51, .cls-52, .cls-53, .cls-54, .cls-55"
class_names = [class_name.strip().lstrip('.') for class_name in classes.split(',')]

# Modify class names in the SVG file
update_svg_classes_and_styles(filename, class_names, filename.split('.')[0])
