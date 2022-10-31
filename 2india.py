import praw
import json
import re
import random
import os
import time
import subprocess
import datetime
import schedule
import traceback
import logging
import requests
from PIL import Image as PIL_Image
import imagehash
from wand.image import Image
from wand.compat import nested
import uuid
# Create and configure logger

# done = []
# for a3 in open("crosspost-done.txt", "r").read().splitlines():
#   done.append(a3)

logging.basicConfig(filename="crosspost-log.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
def lprint(text):
    logger.info(text)
    print(text)

lprint('\n\n\n\n\n\nstarted')

reddit8 = praw.Reddit(user_name='LeakingHub',refresh_token='2236670915560-ldRKkE6DVbArQT7tw9b7Ku4JSTO9Cw',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
reddit10 = praw.Reddit(user_name='SexySlut__nSex',refresh_token='2236667881942-eXSITcy7KEBkKdVk1Skfo-PPtgSotA',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
reddit9 = praw.Reddit(user_name='Shoe_Rack_',refresh_token='2257109827732-xKr4hJqdpntr3d4iizdizy1XVO_4Ng',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
reddit=random.choice([reddit10,reddit8,reddit9])

reddit2 = praw.Reddit(username="Celeb_Sex_Scene1", password="Celeb_Sex_Scen", client_id="k6IVGQK0tRr6AmpW5as2rg", client_secret="KTlypZcuMDPmykIk_N3XRViuzYoiIg", user_agent="scdexeemo", ratelimit_seconds="3649",)
# reddit = praw.Reddit(username="Desi_webseries69", password="Desi_webseries6", client_id="QHmdj47wSZiiMc-CYlZ88g", client_secret="qIGD7IL8KgTmtk29zdAqMwU0JBs3QA", user_agent="GsiI38B", ratelimit_seconds="3649",)
# reddit = praw.Reddit(username="Nicolas_Faisla2", password="Nicolas_Faisla", client_id="TlmHECOiuZzsPA30s9EQ8w", client_secret="jGDuTmhY9oqiW8huwzCNO67HnEVucA", user_agent="scdemso", ratelimit_seconds="3649",)
# reddit = praw.Reddit(username="Latest_webSeries", password="Latest_webSerie", client_id="kGbrMHP8OsnF3ZOkInbxKQ", client_secret="6cxDikojXDNaYMr8ts_XW0M_NJAfnw", user_agent="demo", ratelimit_seconds="3649",)
reddit = praw.Reddit(username="NewTonJhatka-", password="sUenOUWB2791aH", client_id="vXsFz253nOiltDZpW5hl_w",client_secret="RWL6UXLBV52aJHccrGUlHngxtCc6cA", user_agent="demo", ratelimit_seconds="3649",)
# reddit = praw.Reddit(username="Pedophile_prophet-12", password="Pedophile_prophet-1", client_id="4Jes1yQh2VWKg4xGS7wJhg", client_secret="4pptMOTt7yJn2BRuB2tGqywcsKF_QA", user_agent="scdemso", ratelimit_seconds="3649",)
# reddit = praw.Reddit(user_name='HinaKhan-Fapper',refresh_token='2192396328867-nRW6R1RLQ1w3oZjjomnmzos8kC7PwQ',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
# reddit = praw.Reddit(username="Material-Honey9132", password="Material-Honey913", client_id="IhxBUPRXYvV6IT-fTcF1gA", client_secret="E8tKQ2fNuQSKGvCAkCxPu6ryXc-dAw", user_agent="github.com/Damgaard/Reddit-unique-Bots/", ratelimit_seconds="3649",)
def RandomAccount():
#   reddit=random.choice([reddit10,reddit8,reddit9])
#   lprint(reddit.user.me().name)
  subreddit=reddit.subreddit('2india')
  return subreddit


titles=[]
manual_approve=False
hash_array=[]
hash_array_str=[]
watermark=False
video_watermark=False
if video_watermark==True:
    from moviepy.editor import *
count=0
# image_logo = Image(filename='sub.png')
subreddit=reddit.subreddit("2india")
# check_hash = imagehash.average_hash(PIL_Image.open('temp/raw_img.jpg'))
# with open("/home/ubuntu/mum/old_run-py/urls.json") as fh:
#     redgifs_urls = json.load(fh)
#     for item in redgifs_urls:
#         hash_array.append(item)
# hash_array.append(check_hash)
with open("data/crosspost_hashes.json", "r") as file:
    for item in json.load(file):
        hash_array_str.append(item)

last_created_utc=int(time.time())
created_utc=last_created_utc
done = []
# author("/home/ubuntu/mum/IC/invite-authors.txt", "a+")
hourly=[]
h=0
now = datetime.datetime.now()
hour=int(now.strftime("%H"))
subs="TheBollywoodMilfs+SouthIndianAngels+HotIndianWomen+TollywoodCelebrities+SouthIndianBeauty+Marathiactresscum+indiangirls+IndianCelebritySilk+IndianCelebHotScenes+indianActorHaven+HotIndianActresses+Hot_Indian_Angels+Hot_Indian_Angel+FapToDesi+FappOnActress+DesiThunderThighs+DesiPetiteCelebs+desinavelsandbellies+Desijobuds+desiindianslutty+BollywoodCougars+BollywoodUHQonly+SharvariWagh_+TaraSutaria_+katrinakaif+ApsaraBazaar+hotindianceleb+helidaruwala_+JanhviKapoorFc+janhvikapoor+Janhvi_Fap_Club+SaraAliKhanfappers+SaraAliKhanFap+SunnyLeone+NRIBeauties+JacquelineFernandez+SuperModelIndia+IndianActressx+IndianModelsActress+Sareebeauties+IndianCelebScenes+DesiFappedToHer+DesiCelebHub+indiancelebs+HottiesOfTVandYT+BeautifulIndianWomen+faptodesiactress+Bollywoodhottieshub+jerkofftobollywood+IndianActressesHot+bollyarm+reelsgonewild+Meghnakaur+DesiVideshiHottest+SakshiMalikFappers+DesiPetiteBabes+Sana_Saeed_Hot+DesiUnderratedBabes+RadhikaSeth+QueenNushratBharucha+ShraddhaKapoorLegs+shraddhakapoorfap+shreyxa+AliaBhattPics+JanhviKapoorFap+Suhuu+DishaPataniFap+KareenaKapoorFC+nehasharma+AkankshaSharma+TaraSutaria+KanganaRanaut+Bollywoodhotness+mouniroy+JenniferAniston+jhanvikapoor+ParineetiChopra+Aisha_Sharma+ShraddhaShaggers+jacquelinefappers+JacquelineLUST+shraddhakapoor+AnushkaSharma+SexyCelebFemales+karishmasharma+DeepikaPadukone+InstagramHotties+DesiTeen+instaboldreels+DivyaKumarKhosla+Desinude_daily+rivikamani+priyarai+BrownHotties+DeepikaPadukoneFap+AvneetKaur+Saggy+UnderratedInstaGirls+NancyMomolandFap+TamannaBhatia+SareeVsBikini+AishwaryaRaiWorship+KritiSanonLovers+NoraFatehi_FC+MalluBabes+jhanvikapoorfappers+BollywoodFashion+KiaraAdvaniFap+Dakini+IndianAnchorsFap+DesiCelebBattles+KritiSanonFap+KritiSanon+ShagOnHotties+JerkOffToDesiCelebHub+desitraditionallysexy+palaktiwari+NehaSharmaFans+EshaGupta_Fap+desigentlemanboners+SamanthaAkkineni+MuslimCuckoldCaptions+AnanyaPandeyFap+KritiKharbanda+Desibacklessfap+indianmilfs+ShriyaSaran+DesiDiasporaOnly+SonakshiSinhaFap+Indianactressgalaxy+MadhuriDixit+Kajal_aggarwal+indiannudescenes"
subs="2india|IndianCelebScenes+IndianCelebHotScenes"
subs="SouthIndianAngels+HotIndianWomen+TollywoodCelebrities+SouthIndianBeauty+Punjabiactresses+Marathiactresscum+indiangirls+IndianCelebritySilk+IndianCelebHotScenes+indianActorHaven+HotIndianActresses+Hot_Indian_Angels+Hot_Indian_Angel+FapToDesi+FappOnActress+DesiThunderThighs+DesiPetiteCelebs+desinavelsandbellies+Desijobuds+desiindianslutty+BollywoodCougars+BollywoodUHQonly+SharvariWagh_+TaraSutaria_+katrinakaif+ApsaraBazaar+hotindianceleb+helidaruwala_+JanhviKapoorFc+janhvikapoor+Janhvi_Fap_Club+SaraAliKhanfappers+SaraAliKhanFap+SunnyLeone+JacquelineFernandez+SuperModelIndia+IndianActressx+IndianModelsActress+Sareebeauties+IndianCelebScenes+DesiFappedToHer+DesiCelebHub+indiancelebs+HottiesOfTVandYT+BeautifulIndianWomen+faptodesiactress+Bollywoodhottieshub+jerkofftobollywood+IndianActressesHot+bollyarm+reelsgonewild+Meghnakaur+DesiVideshiHottest+DesiPetiteBabes+Sana_Saeed_Hot+DesiUnderratedBabes+RadhikaSeth+QueenNushratBharucha+ShraddhaKapoorLegs+shraddhakapoorfap+shreyxa+AliaBhattPics+JanhviKapoorFap+Suhuu+DishaPataniFap+KareenaKapoorFC+nehasharma+AkankshaSharma+TaraSutaria+KanganaRanaut+Bollywoodhotness+mouniroy+JenniferAniston+jhanvikapoor+ParineetiChopra+Aisha_Sharma+ShraddhaShaggers+jacquelinefappers+JacquelineLUST+shraddhakapoor+AnushkaSharma+SexyCelebFemales+karishmasharma+DeepikaPadukone+InstagramHotties+DesiTeen+instaboldreels+DivyaKumarKhosla+Desinude_daily+rivikamani+priyarai+BrownHotties+DeepikaPadukoneFap+AvneetKaur+Saggy+UnderratedInstaGirls+NancyMomolandFap+TamannaBhatia+SareeVsBikini+AishwaryaRaiWorship+KritiSanonLovers+NoraFatehi_FC+MalluBabes+jhanvikapoorfappers+BollywoodFashion+KiaraAdvaniFap+Dakini+IndianAnchorsFap+DesiCelebBattles+KritiSanonFap+KritiSanon+ShagOnHotties+JerkOffToDesiCelebHub+desitraditionallysexy+palaktiwari+NehaSharmaFans+EshaGupta_Fap+desigentlemanboners+SamanthaAkkineni+MuslimCuckoldCaptions+AnanyaPandeyFap+KritiKharbanda+Desibacklessfap+indianmilfs+ShriyaSaran+DesiDiasporaOnly+SonakshiSinhaFap+Indianactressgalaxy+MadhuriDixit+Kajal_aggarwal+indiannudescenes"
def invite(author):
    try:
      if author not in authors:
        reddit.redditor(author).message(subject="Your Posts Are Good, I liked them", message="Hi I seen your posts and Liked Them, Could You please Post In r/2india also.", from_subreddit="u_Latest_webSeries")
        authors.append(author)
        lprint(author)
        f.write(author+"\n")
        time.sleep(60)
    except Exception as e:
      lprint('\nerror\n')
      lprint(e)
      pass


def hourly_submit():
    global hour, hourly
    now = datetime.datetime.now()
    if int(now.strftime("%H")) !=hour and len(hourly)>1:
        hour=int(now.strftime("%H"))
        logger.info("Hourly Submission "+ str(len(hourly)))
        submission = subreddit.submit_gallery('Hourly Albume ', images=hourly)
        lprint("Hourly submission permalink  "+ submission.permalink)
        hourly=[]

def hourly_submission(url):
    file_h=str(uuid.uuid4())+".jpg"
    open("temp/"+file_h, 'wb').write(requests.get(url).content)
    hourly.append({"image_path": "temp/"+file_h})



def hash_check(file, include=True):
        hash = imagehash.average_hash(PIL_Image.open(file))
    # cutoff = 5  # maximum bits that could be different between the hashes. 
        # if hash in hash_array:
        if str(hash) in hash_array_str:
            lprint('images are similar')
            return False
        else:
            lprint('images are not similar')
            if include==True:
                hash_array_str.append(str(hash))
                with open("data/crosspost_hashes.json", "w+") as file:
                    file.write(json.dumps(hash_array_str, indent = 1))
            return True

def title_filter(title):
    split=re.split("\[Join|Join|r/|IndianCeleb|Thebolly", title, re.IGNORECASE)
    title=split[0]
    # title=re.sub(" in "," , ", title, re.IGNORECASE)
    # .sub(" hot ", " sexy ", title, re.IGNORECASE)
    # .sub(" sexy ", " hot ", title, re.IGNORECASE)
    # .sub(" sex ", " love making ", title, re.IGNORECASE)
    title_array={
        " hot ":" sexy ",
        " sexy ":" hot ",
        " sex":" love making ",
        " cutie ":" Cute ",
        " kissing ":" smooch ",
        " rand":"Ramd",
        " Juicy ":" Full of Milk ",
        " Scene ": " Perfect Scene ",
        " amazing ": " Awsome"
        }
    for data in title_array.keys():
      title = re.sub(f"{data}",f"{title_array[data]}", title, re.IGNORECASE)
    return title #+ " r/2india"


def Gallery(item, title):
    subreddit=RandomAccount()
    submission=None
    g = 0
    gallery = []
    for i2 in item.media_metadata.items():
        # for i in post.media_metadata.items():
        g += 1
        iurl = i2[1]['p'][0]['u']
        iurl = iurl.split("?")[0].replace("preview", "i")
        image = str(g) + 'gallery.jpg'
        open("temp/"+image, 'wb').write(requests.get(iurl).content)
        file="temp/"+image
        if hash_check("temp/"+image)==True:
            if watermark==True:
                wimage = Image(filename=file)
                wimage=wimage.clone()
                img=image_logo.clone()
                h=int(wimage.height/50)
                div=int(img.width/img.height)
                img.resize(int(h*div), h, blur = 1)
                wimage.watermark(img, 0.75, int(wimage.width/7), int(wimage.height/1.5))
                wimage.save(filename="temp/"+"new_"+image)
                image="temp/"+"new_"+image
            body = {"image_path": file}
            gallery.append(body)
    if len(gallery) > 2:
        submission = subreddit.submit_gallery(title, images=gallery)#, flair_id='0999c656-1d4d-11ed-9b9c-9610c5ec960f')
        return submission

def Video(item, title):
    url=item.url
    subreddit=RandomAccount()
    submission=None
    os.system("rm -rf raw_main.mp4")
    if 'v.redd.it' in url:
        os.system("yt-dlp '" + url + "/DASHPlaylist.mpd' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ") # > /dev/null 2> /dev/null")
    # if 'redgifs' in url:
    #   os.system("youtube-dl '" + url + "' -o raw_main.mp4 || yt-dlp '" + url + "' -o raw_main.mp4 ")
    # else:
    #     os.system("yt-dlp '" + url + "' -o raw_main.mp4 ")#> /dev/null 2> /dev/null")
        subprocess.call(['ffmpeg', '-i', 'raw_main.mp4', '-ss', '00:00:01.000', '-vframes','1', 'watthumb.png', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # # subprocess.call(['ffmpeg', '-i', 'raw_main.mp4', '-ss', '00:00:02.000', '-vframes','1', 'temp/hash0.png', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # # subprocess.call(['ffmpeg', '-i', 'raw_main.mp4', '-ss', '00:00:05.000', '-vframes','1', 'temp/hash1.png', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        file='raw_main.mp4'
        if os.path.exists(file)!=True:
            raise Exception("No Video File Found")
        if hash_check('watthumb.png')==True:
    #     if watermark==True:
    #         file='main.mp4'
    #         os.system("time ffmpeg -i raw_main.mp4 -vf 'drawtext=:text='r\/2india':fontcolor=#e7e7e7@0.5:fontsize=h/60:x=w-tw-10:y=h-th-10' -preset ultrafast -r 15 -codec:a copy main.mp4 -y || cp raw_main.mp4 main.mp4") #x=(w-text_w)/4:y=(h-th)/1.5
    #         # clip = VideoFileClip('main.mp4') 
    #         # lprint("audio fps: "+ str(clip.audio.fps))
    #         # os.system("ffmpeg -i /home/ubuntu/mum/waste/media/logo.mp4 -map 0 -c:v copy -c:a aac -ar "+ str(clip.audio.fps) +" /home/ubuntu/mum/waste/media/new_logo.mp4 -y")
    #         # os.system("mkvmerge -o 'main.mp4'  'raw_main.mp4' \+ '/home/ubuntu/mum/waste/media/new_logo.mp4'")
    #     if video_watermark==True:
    #         #image
    #         clip = VideoFileClip("raw_main.mp4")
    #         if clip.duration < 7200:
    #           height = clip.h
    #           width = clip.w
    #           fontsize=int((height+width)/90)
    #           logo = TextClip("r/2india",font="Courier-Bold", fontsize = fontsize, color = 'black') 
    #           logo = logo.set_duration(clip.duration).set_opacity(.25).set_pos((int(height/5),int((width/5)))) #.set_pos('center')
    #           video = CompositeVideoClip([clip, logo])
    #           video.write_videofile("main.mp4")
    #           file='main.mp4'
                submission = subreddit.submit_video(title, video_path=file, thumbnail_path='watthumb.png') # , flair_id='c94e84ce-1d4c-11ed-ac70-1a7606ef742f')
            # os.system("rm -rf file.mp4 && yt-dlp '" + url + "/DASHPlaylist.mpd' -o file.mp4 || yt-dlp '" + url + "' -o file.mp4 ") # > /dev/null 2> /dev/null")
            # url=upload_from_file(authorize_me(), "raw_main.mp4")
            # submission = subreddit.submit(title, url=url)
        # if 'v.redd.it' not in url:
        #     submission = subreddit.submit(title, url=url)
    # if 'v.redd.it' in url:
    #     os.system("rm -rf file.mp4 && yt-dlp '" + url + "/DASHPlaylist.mpd' -o file.mp4 || yt-dlp '" + url + "' -o file.mp4 ") # > /dev/null 2> /dev/null")
    #     url=upload_from_file(authorize_me(), "file.mp4")
    #     submission = subreddit.submit(title, url=url)
    return submission


def Image_submission(item, title):
    url=item.url
    subreddit=RandomAccount()
    submission=None
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
        # lprint("check")
        if watermark==True:
            wimage = Image(filename=file)
            wimage=wimage.clone()
            img=image_logo.clone()
            h=int(wimage.height/50)
            div=int(img.width/img.height)
            img.resize(int(h*div), h, blur = 1)
            wimage.watermark(img, 0.75, int(wimage.width/7), int(wimage.height/1.5))
            wimage.save(filename ='temp/img.jpg')
            file='temp/img.jpg'
            # subprocess.call("ffmpeg -i raw_img.jpg -vf 'drawtext=fontfile=/path/to/font.ttf:text='r\/2india':fontcolor=white:fontsize=24:x=(w-text_w)/2:y=h-th-5' -codec:a copy img.jpg -y >> log2.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    # submission = reddit.subreddit("BollywoodMilfsHub").submit_image(title, file, flair_id='edacfc06-1d4c-11ed-b0bb-4611b5aeafec')
    # submission = subreddit.submit(title, url=submission.url)
    if hash_check(file)==True:
        # submission = subreddit.submit(title, url=url)
        submission = subreddit.submit_image(title, file)
        
    return submission


# for item in reddit.subreddit(subs).stream.submissions(skip_existing=True):
def fetch():
  global last_created_utc, subs, created_utc, count, done
  post_type='None'
  lprint("count "+str(count)+" : "+ str(len(done)))
  count+=1
  array=[]
  array2=[]
  for item in reddit.subreddit("IndiaSpeaks+Sham_Sharma_Show+indiasocial+India+indianews").new(limit=25): #+IndianCelebHotScenes
    # if bool(re.search("faptodesiactress",str(item.subreddit), re.IGNORECASE))==True:
        array.append(item)
        array2.append({"title":item.title, "url": item.url, "permalink":item.permalink})
#   with open("data/crosspost_array2.txt", "w+") as file:
#     file.write(json.dumps(array2, indent=1))
  print(len(array))
  for item in array:
    if count==1:
        done.append(item.id)
    else:
      if item.id not in done: 
        try:
            # lprint(done)
            lprint(item.permalink)
            done.append(item.id)
            created_utc=item.created_utc
            submission=None
            sub=re.split('/', item.permalink)[2]
            # main_subs="TheBollywoodMilfs|SouthIndianBeauty|HotIndianWomen|IndianCelebHotScenes|desinavelsandbellies|SakshiMalikFappers|IndianCelebScenes|faptodesiactress|palaktiwari|NehaSharmaFans|EshaGupta_Fap"
            # main_subs="SouthIndianAngels|HotIndianWomen|TollywoodCelebrities|SouthIndianBeauty|Punjabiactresses|IndianCelebritySilk|IndianCelebHotScenes|indianActorHaven|HotIndianActresses|Hot_Indian_Angels|Hot_Indian_Angel|FapToDesi|FappOnActress|DesiThunderThighs|DesiPetiteCelebs|desinavelsandbellies||BollywoodCougars|BollywoodUHQonly|SharvariWagh_|TaraSutaria_|katrinakaif|ApsaraBazaar|hotindianceleb|helidaruwala_|JanhviKapoorFc|janhvikapoor|Janhvi_Fap_Club|SaraAliKhanfappers|SaraAliKhanFap|JacquelineFernandez|SuperModelIndia|IndianActressx|IndianModelsActress|Sareebeauties|IndianCelebScenes|DesiFappedToHer|DesiCelebHub|indiancelebs|HottiesOfTVandYT|BeautifulIndianWomen|faptodesiactress|Bollywoodhottieshub|jerkofftobollywood|IndianActressesHot|bollyarm|reelsgonewild|Meghnakaur|DesiVideshiHottest|DesiPetiteBabes|Sana_Saeed_Hot|DesiUnderratedBabes|RadhikaSeth|QueenNushratBharucha|ShraddhaKapoorLegs|shraddhakapoorfap|shreyxa|AliaBhattPics|JanhviKapoorFap|Suhuu|DishaPataniFap|KareenaKapoorFC|nehasharma|AkankshaSharma|TaraSutaria|KanganaRanaut|Bollywoodhotness|mouniroy|JenniferAniston|jhanvikapoor|ParineetiChopra|Aisha_Sharma|ShraddhaShaggers|jacquelinefappers|JacquelineLUST|shraddhakapoor|AnushkaSharma|SexyCelebFemales|karishmasharma|DeepikaPadukone|InstagramHotties|DesiTeen|instaboldreels|DivyaKumarKhosla|Desinude_daily|rivikamani|priyarai|BrownHotties|DeepikaPadukoneFap|AvneetKaur|Saggy|UnderratedInstaGirls|TamannaBhatia|SareeVsBikini|AishwaryaRaiWorship|KritiSanonLovers|NoraFatehi_FC|MalluBabes|jhanvikapoorfappers|BollywoodFashion|KiaraAdvaniFap|Dakini|IndianAnchorsFap|DesiCelebBattles|KritiSanonFap|KritiSanon|ShagOnHotties|JerkOffToDesiCelebHub|desitraditionallysexy|palaktiwari|NehaSharmaFans|EshaGupta_Fap|desigentlemanboners|SamanthaAkkineni|MuslimCuckoldCaptions|AnanyaPandeyFap|KritiKharbanda|Desibacklessfap|indianmilfs|ShriyaSaran|DesiDiasporaOnly|SonakshiSinhaFap|Indianactressgalaxy|MadhuriDixit|Kajal_aggarwal|indiannudescenes"
            # if sub == "2india":
            #     titles.append(title)
            #     newton=title_filter(title)
            if bool(re.search('porn|desi|DM|msg me|call me|link|comment',item.title, re.IGNORECASE))==False: #bool(re.search(main_subs,sub, re.IGNORECASE))==True and 
                    sub='2india'
                    url=item.url
                    title=item.title #+" "+item.author.name
                    permalink=item.permalink
                # title=title_filter(title)
                # if title not in titles:
                    titles.append(title)
                    print(item.is_self)
                    if item.is_self==True:
                        submission=subreddit.submit(title, selftext=item.selftext)
                    # elif bool(re.search("redgifs.com|gyfcat.com|.mp4|v.redd.it", url)) == True:
                    #     post_type="Video"
                    #     lprint(post_type)
                    #     submission=Video(item, title)
                    #     sl = random.randint(2000, 2500)
                    elif bool(re.search("i.redd.it|.gif", url)) == True:
                        # hourly_submission(url)
                        post_type="Image/GIF"
                        lprint(post_type)
                        submission=Image_submission(item, title)
                        sl = random.randint(1000, 1500)
                    elif 'gallery' in url:
                        post_type="Gallery"
                        submission=Gallery(item, title)
                        sl = random.randint(1700, 2500)
                    elif item.url !=None and bool(re.search("redgifs.com|reddit.com|gyfcat.com|.mp4|v.redd.it", url)) != True:
                        submission=subreddit.submit(title, url=item.url)
                    
                    #mod approve
                    
                    if submission!=None:
                        # item.hide()
                        lprint(item.permalink)
                        lprint(submission.permalink)
                        if manual_approve==True:
                                time.sleep(10)
                                submission2 = reddit1.submission(submission.id)
                                submission2.mod.approve()
                                lprint("mod approved :- "+ str(submission.permalink))
                        lprint(item.permalink+" Submitted as  "+submission.permalink+ " Type: "+post_type)
                        # if post_type!="Image/GIF" or post_type!="Gallery":
                        #     time.sleep(3000)
                    else:
                        lprint("submission is None "+ " Type: "+post_type)
                    # now = datetime.datetime.now()
                # else:
                #     lprint("title already Submitted ")
        except Exception as e:
            lprint(e)
            traceback.print_exc()
            pass
  lprint("done count "+str(count)+" : "+ str(len(done))+"\n")
  last_created_utc=created_utc

# fetch()
# schedule.every(5).minutes.do(fetch)

while True:
    fetch()
    sleep_time=random.randint(3,5)
    for i in range(60*sleep_time,0,-1):
        time.sleep(1)
        print(f"{str(i)} Seconds Left Out of {str(60*sleep_time)}", end='\r')


    if count==24*(60/5):
        ps=0
        lprint("cleaning")
        for post in reddit.user.me().submissions.new(limit=500):
            ps+=1
            if post.is_robot_indexable==False and ps > 25: # and post.created_utc:
                post.delete()
                print(f"deleted  {post.permalink}")
        count=2
#     schedule.run_pending()
#     time.sleep(1)
