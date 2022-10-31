from flask import Flask,request
import praw, json, time, os, requests, re
import logging
 
logging.basicConfig(filename="log.txt",format='%(asctime)s %(message)s',filemode='a') ; logger = logging.getLogger() ; logger.setLevel(logging.DEBUG) ; logger.info("\n------------------------\n")


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hedllo from Koyeb'

@app.route('/video')
def video():
    title=request.args.get('title') ; url=request.args.get('url')
    os.system(f"youtube-dl {url} -o main.mp4")
    # # submission=reddit.subreddit(sub).submit_video(title, 'main.mp4', thumbnail_path='watthumb.png')    
    return str(os.listdir("./"))



if __name__ == "__main__":
    app.run(port=5002)

hp_pO4I10sWhOwRAUZfijNbdpcufBXHtW4KJKfR