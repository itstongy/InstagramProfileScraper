from InstagramAPI import InstagramAPI
import time

username = ""
password = ""

InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

myposts=[]
has_more_posts = True
max_id=""

while has_more_posts:
    InstagramAPI.getSelfUserFeed(maxid=max_id)
    if InstagramAPI.LastJson['more_available'] is not True:
        has_more_posts = False #stop condition
        print("stopped")

    max_id = InstagramAPI.LastJson.get('next_max_id','')
    myposts.extend(InstagramAPI.LastJson['items']) #merge lists
    time.sleep(2) # Slows the script down to avoid flooding the servers

print(len(myposts))




copynpaste = ''
for posts in range(len(myposts)):
    print(posts)
    loc = ''
    try:
        if (myposts[posts]['image_versions2']['candidates'][0]['url']):
            img = myposts[posts]['image_versions2']['candidates'][0]['url']
    except:
        print('no single img')
    try:
        if (myposts[posts]['carousel_media'][0]['image_versions2']['candidates'][0]['url']):
            img = myposts[posts]['carousel_media'][0]['image_versions2']['candidates'][0]['url']
    except:
        print('no2')
    likes = myposts[posts]['like_count']
    comments = myposts[posts]['comment_count']
    try:
        if(myposts[posts]['location']['name']):
            loc = myposts[posts]['location']['name']
            print(loc)
            print(myposts[posts]['location']['name'])
    except:
        print('noLoc')
    dateVal = time.strftime("%d-%m-%Y", time.localtime(myposts[posts]['caption']['created_at']))
    timeVal = time.strftime("%H:%M", time.localtime(myposts[posts]['caption']['created_at']))

    copynpaste+= str(img) + '\t' + str(likes) + '\t' + str(comments) + '\t' + str(loc) + '\t' + str(dateVal) + '\t' + str(timeVal) + '\n'
    #copynpaste+=str(str(myposts[posts]['image_versions2']['candidates'][0]['url']) + "\t" + str(myposts[posts]['like_count']) + "\t" + str(myposts[posts]['comment_count']) + "\t" + str(myposts[posts]['location']['name'])+ "\t" + str(time.strftime("%d-%m-%Y %H:%M", time.localtime(myposts[posts]['caption']['created_at']))))


dataF = open('copy.txt','w')
dataF.write(str(copynpaste))
dataF.close()
