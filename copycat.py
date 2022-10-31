import praw, os, subprocess, time, requests
from PIL import Image as PIL_Image
import imagehash, re
import sys
sys.path.insert(1, '/home/ubuntu/mum/IC')
import gyfcat

reddit = praw.Reddit(user_name='Living-Field-2070',refresh_token='2315505442146-HPb7mc4GRHcpm6DEwvPNTn7Fn-DJXg',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
subreddit=reddit.subreddit('Bharat_verse')
def RandomAccount():
  subreddit=reddit.subreddit('Bharat_verse')
  return subreddit

def hash_check(a):
    return True


def Gallery(item, title):
    subreddit=RandomAccount()
    submission=None
    g = 0
    gallery = []
    for i2 in item.media_metadata.items():
        g += 1
        iurl = i2[1]['p'][0]['u']
        iurl = iurl.split("?")[0].replace("preview", "i")
        image = str(g) + 'gallery.jpg'
        open("temp/"+image, 'wb').write(requests.get(iurl).content)
        file="temp/"+image
        # if hash_check("temp/"+image)==True:
        body = {"image_path": file}
        gallery.append(body)
    if len(gallery) > 1:
        submission = subreddit.submit_gallery(title, images=gallery)#, flair_id='0999c656-1d4d-11ed-9b9c-9610c5ec960f')
        return submission

def Video(url, title):
    subreddit=RandomAccount() ; submission=None ; os.system("rm -rf raw_main.mp4")
    if 'v.redd.it' in url:
        print("yt-dlp '" + url + "/DASHPlaylist.mpd' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ")
        os.system("yt-dlp '" + url + "/DASHPlaylist.mpd' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ") # > /dev/null 2> /dev/null")
    if 'redgifs' in url:
      os.system("youtube-dl '" + url + "' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ")
    else:
        os.system("yt-dlp '" + url + "' -o raw_main.mp4 ")#> /dev/null 2> /dev/null")
    subprocess.call(['ffmpeg', '-i', 'raw_main.mp4', '-ss', '00:00:01.000', '-vframes','1', 'watthumb.png', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    file='raw_main.mp4'
    if os.path.exists(file)!=True:
        raise Exception("No Video File Found")
    if hash_check('watthumb.png')==True:
            submission = subreddit.submit_video(title, video_path=file, thumbnail_path='watthumb.png') # , flair_id='c94e84ce-1d4c-11ed-ac70-1a7606ef742f')
    return submission


def Image_submission(url, title):
    subreddit=RandomAccount(); submission=None
    if bool(re.search(".gif", url)) == True:
        r=requests.get(url)
        if r.status_code==200:
            open('temp/raw_img.gif', 'wb').write(r.content)
        else:
            raise Exception("404 Not Found")
        file="temp/raw_img.gif"
    else:
        r=requests.get(url)
        if r.status_code==200:
            open('temp/raw_img.jpg', 'wb').write(r.content)
        else:
            raise Exception("404 Not Found")
        file='temp/raw_img.jpg'
    if hash_check(file)==True:
        submission = subreddit.submit_image(title, file)
    return submission

def main(url, title,item=None):
    if bool(re.search("i.redd.it|.gif", url)) == True:
        submission=Image_submission(url, title)
    elif 'gallery' in url:
        post_type="Gallery"
        print(post_type)
        submission=Gallery(item, title)
    elif bool(re.search("redgifs.com|reddit.com|gyfcat.com|.mp4|v.redd.it", url)) == True:
        submission=Video(url, title)
    else: 
        submission=subreddit.submit(title, url=item.url)
    print(submission)

url="https://www.reddit.com/r/IndiaSpeaks/comments/yh9xhf/hindi_as_a_mother_tonguehistoric_vs_2022/"
submission=reddit.submission(url=url)
print(submission.url)
main(submission.url, submission.title,item=submission)


# Image_submission(
#     url=submission.url,
#     title=submission.title
# )
# Video(
#     url="https://v.redd.it/hzjdi3ans4p81",
#     title="Train Journey🚉 ft. Middle Class❤️ "
# )


# Image_submission(
#     url="https://i.redd.it/mxa9t5vlyvw91.jpg",
#     title="Just a regular sunset, on my way home"
# )
# Image_submission(
#     url="https://i.imgur.com/b6qKQD8.jpg",
#     title="An Ad posted as a news in paper, The facts are fake"
# )

# Gallery(
#     item=submission,
#     title=submission.title
# )
'''
title="spam"
url="https://i.redd.it/ghq06xz9z2e81.png"

r=requests.get(url)
if r.status_code==200:
    open('temp/raw_img.jpg', 'wb').write(r.content)
else:
    raise Exception("404 Not Found")
file='temp/raw_img.jpg'
submission = subreddit.submit_image(title, file)
print(submission.url)

url="https://v.redd.it/l0k0acgvj4p81"

os.system("rm -rf raw_main.mp4")
if 'v.redd.it' in url:
    print("yt-dlp '" + url + "/DASHPlaylist.mpd' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ")
    os.system("yt-dlp '" + url + "/DASHPlaylist.mpd' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ") # > /dev/null 2> /dev/null")
if 'redgifs' in url:
    os.system("youtube-dl '" + url + "' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ")
else:
    os.system("yt-dlp '" + url + "' -o raw_main.mp4 ")#> /dev/null 2> /dev/null")

gyfcat.upload_from_file(gyfcat.authorize_me(), "raw_main.mp4")
'''