import pafy
import pymongo
from pymongo import MongoClient
import FWStackTemplateGenerator

client = MongoClient('localhost', 27017)
db = client.fridayVideos
stackTemplate = FWStackTemplateGenerator


def parse(url, category):
    video = pafy.new(url)
    best_video = video.getbest()
    video_object = {'yt_id':video.videoid,
                    'url': best_video.url,
                    'category': category,
                    'title': best_video.title,
                    'duration': video.duration,
                    'description': video.description,
                    'thunmbnail_url':video.bigthumbhd,
                    'dimensions':best_video.dimensions}
                    
    videos = db.videos
    video_id = video.videoid
    videoExist = exist(video_id)
    if videoExist == False:
        video_object_id = videos.insert_one(video_object).inserted_id
        print (videos.find())
        video = db.videos.find_one({'yt_id': video_id})
        stackTemplate.addVideo(video)
        return ('Added')
    else:
        return ('This Video existed in the list')

def exist(video_id):
    video = db.videos.find_one({'yt_id': video_id})
    if video == None:
        return False
    return True