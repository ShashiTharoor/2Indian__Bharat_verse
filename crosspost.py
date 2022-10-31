import praw, os, subprocess, time, requests


reddit = praw.Reddit(user_name='Living-Field-2070',refresh_token='2315505442146-HPb7mc4GRHcpm6DEwvPNTn7Fn-DJXg',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)


count=0
done=[]
def fetch():
    global count, done
    count+=1
    print("count "+str(count)+" : "+ str(len(done)))
    for item in reddit.subreddit("IndiaSpeaks+Sham_Sharma_Show+indiasocial+India+indianews").new(limit=25): #+IndianCelebHotScenes
        if count==1:
            done.append(item.id)
        else:
            if item.id not in done: 
                done.append(item.id)
                submission=reddit.subreddit("Bharat_verse").submit(item.title, url=f"https://www.reddit.com{item.permalink}")
                print(submission.permalink)
                time.sleep(10)


while True:
    fetch()
    time.sleep(300)