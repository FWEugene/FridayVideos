import xml.etree.ElementTree as ET
import pymongo
from pymongo import MongoClient

filename = './static/templates/stackTemplate.xml'

def addVideo(videoObject):
    
    tree = ET.ElementTree(file='./static/templates/stackTemplate.xml')
    root = tree.getroot()
    grids = root.iter('grid')
    
    
    for grid in grids:
        section = grid.find('section')
        newlockup = lockupTemplate()
        img = newlockup.find('img')
        print (videoObject)
        newlockup.set('videoIdentifier', videoObject['yt_id'])
        
        img.set('src', videoObject['thunmbnail_url'])
        dimensions = videoObject['dimensions']
        img.set('width', "320")
        img.set('height', "180")

        title = newlockup.find('title')
        title.text = videoObject['title']
    
        section.append(newlockup)
                
    with open(filename, 'w', encoding='utf-8') as file:
        tree.write(file, xml_declaration=True, encoding='unicode')
        
    ET.dump(tree)
        
    return



            
def lockupTemplate():
    lockup = ET.fromstring('<lockup videoIdentifier=""><img src="" width="" height="" /><title></title></lockup>')
    return lockup

    