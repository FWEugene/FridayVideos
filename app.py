from bottle import Bottle
from bottle import template
from bottle import static_file
from bottle import route, run, request, abort
import pymongo
from pymongo import MongoClient
import youtubeParser


app = Bottle()
client = MongoClient('localhost', 27017)
db = client.fridayVideos
ytparser= youtubeParser


@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')


@app.get('/addVideo') 
def addVideo():
    return '''
    
    <!DOCTYPE HTML>
    <head>
        <title>Future Workshops Friday Videos</title>
        <link rel = "stylesheet" type="text/css" href="./static/styles.css">
    </head>
    <body>
        <h1>Add new friday video</h1>
       <form action="/addVideo" method="post">
           <ul class="form-style-1">
            <li> 
                <label for="name">Youtube Video URL:</label>
                <input name="yturl" type="text" class="field-long" /><br>
            </li>
            </li>
                <label for="name">Category:</label>
                <select name="category" class="field-select">
                   <option>TED Talks</option>
                   <option>Nature</option>
                   <option>Science</option>
                </select>
            </li>
            <li>
                <input type="submit" value="Add Video" />
            </li>
        </ul>
       </form>
    </body>
    '''

@app.post('/addVideo') 
def do_addVideo():
    video_url = request.forms.get('yturl')
    category = request.forms.get('category')
    success = ytparser.parse(video_url, category)
    return success


@app.route('/xml')
def xml():
    response.headers['Content-Type'] = 'xml/application'

    return xml_content_whatever
  
run(app, host='localhost', port=8080, reloader=True)