import xml.etree.ElementTree as ET
import xml.etree
import sys

filename = './static/templates/stackTemplate.xml'


tree = ET.ElementTree(file=filename)
root = tree.getroot()
grids = root.iter('grid')

for grid in grids:
    section = grid.find('section')
    
    lockup = ET.fromstring('<lockup videoIdentifier=""><img src="" width="" height="" /><title></title></lockup>')
    img = lockup.find('img')
    lockup.set('videoIdentifier', 'QWedsdvdfvertert')

    img.set('src', 'QWedsdvdfvertert')
    img.set('width', 'QWedsdvdfvertert')
    img.set('height', 'QWedsdvdfvertert')

    title = lockup.find('title')
    title.text = "asdasdasdasdasd"
    
    section.append(lockup)
         
         
with open(filename, 'w', encoding='utf-8') as file:
    tree.write(file, xml_declaration=True, encoding='unicode')

ET.dump(tree)
    