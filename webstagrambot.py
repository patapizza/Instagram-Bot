#!/usr/bin/python

'''
Cranklin's Instagram Bot v.1.0
==============================
Check www.cranklin.com for updates


This bot gets you more likes and followers on your Instagram account.  

Requirements:
- python > 2.6 but < 3.0
- pycurl library
- web.stagram.com login prior to using the bot

Instructions:
- make sure you have the correct version of Python installed
- make sure you have the pycurl library installed
- log into web.stagram.com with your instagram account and approve the app
- edit between lines 42 and 52
- from the command line, run "python webstagram.py"
- enjoy!

v1.0 updates:
- added browser agent randomizer
- added optional sleep timer 
- added optional hashtag limiter
- added a couple extra additions for some people experiencing SSL errors.  (thanks Charlie)
*** thank you Nick, John, Max, Shahar, Charlie for the help
'''

import os
import psycopg2
import pycurl
import cStringIO
import re
import random
import time
import sys

##### EDIT THESE BELOW

# your instagram username and password
username = "username"
password = "password"

MAX_TRIES = 3

#set a sleep timer between each like.  Set value to 0 if you don't want it to sleep at all
sleeptimer = 5

#set a like limit per hashtag.  Set value to 0 if you don't want a limit
hashtaglikelimit = 100

#your list of hashtags

hashtags = ["ootd","outfit","jeans","short","clothes","dress","dresses","swag","smile","fashion","mode","instalike","girly","ootd","ootn","selfie","style","stylee","pretty","nice","instacool","cheveux","ciel","beauty","beaute","famille","bella","look","lookboot","tenuedujour","tenue","moi","soldes","shopping","shop","clothing","zara","abercrombie","fitch","hollister"]

comments = ["How cute! <3\nxoxo",
            "Love it!"]

spam_comments = ["famest.com",
                 "Join us on famest.com!"]

##### NO NEED TO EDIT BELOW THIS LINE

browsers = ["IE ","Mozilla/","Gecko/","Opera/","Chrome/","Safari/"]
operatingsystems = ["Windows","Linux","OS X","compatible","Macintosh","Intel"]

def connect(params):
    con = None
    try:
        print('--- Connecting...')
        con = psycopg2.connect(params)
        print('--- Connected.')
    except psycopg2.DatabaseError as e:
        print('Error {}'.format(e))
    return con

def login():
    try:
        os.remove("pycookie.txt")
    except:
        pass

    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://web.stagram.com")
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
    c.setopt(pycurl.USERAGENT, useragent)
    c.perform()
    curlData = buf.getvalue()
    buf.close()

    clientid = re.findall(ur"href=\"https:\/\/api.instagram.com\/oauth\/authorize\/\?client_id=([a-z0-9]*)&redirect_uri=http:\/\/web.stagram.com\/&response_type=code&scope=likes\+comments\+relationships\">LOG IN",curlData)
    instagramlink = re.findall(ur"href=\"([^\"]*)\">LOG IN",curlData)




    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, instagramlink[0])
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
    c.setopt(pycurl.USERAGENT, useragent)
    c.perform()
    curlData = buf.getvalue()
    buf.close()

    postaction = re.findall(ur"action=\"([^\"]*)\"",curlData)
    csrfmiddlewaretoken = re.findall(ur"name=\"csrfmiddlewaretoken\" value=\"([^\"]*)\"",curlData)





    postdata = 'csrfmiddlewaretoken='+csrfmiddlewaretoken[0]+'&username='+username+'&password='+password

    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://instagram.com"+postaction[0])
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.setopt(pycurl.REFERER, "https://instagram.com/accounts/login/?next=/oauth/authorize/%3Fclient_id%3D"+clientid[0]+"%26redirect_uri%3Dhttp%3A//web.stagram.com/%26response_type%3Dcode%26scope%3Dlikes%2Bcomments%2Brelationships")
    useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
    c.setopt(pycurl.USERAGENT, useragent)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, postdata)
    c.setopt(pycurl.POSTFIELDSIZE, len(postdata))
    #c.setopt(pycurl.VERBOSE, True)
    c.perform()
    curlData = buf.getvalue()
    buf.close()

def comment(mode):
    params = "dbname=db host=localhost port=5432 user=user password=password"

    con = connect(params)
    if not con:
        sys.exit(1)
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    seen = [name for uid, name in cur.fetchall()]

    commentcount = 0
    for tag in hashtags:
        hashtagcomments = 0
        nextpage = "http://web.stagram.com/tag/" + tag + "/?vm=list"
        while nextpage != False:
            print "Retrieving page " + nextpage + "..."
            buf = cStringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, nextpage)
            c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
            c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
            c.setopt(pycurl.WRITEFUNCTION, buf.write)
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            c.setopt(pycurl.ENCODING, "")
            c.setopt(pycurl.SSL_VERIFYPEER, 0)
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
            useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
            c.setopt(pycurl.USERAGENT, useragent)
            c.perform()
            curlData = buf.getvalue()
            buf.close()
            print "...done."

            nextpagelink = re.findall(ur"<a href=\"([^\"]*)\" rel=\"next\">Earlier<\/a>",curlData)
            nextpage = "http://web.stagram.com"+nextpagelink[0] if len(nextpagelink) > 0 else False

            commentdata = re.findall(ur"<textarea name=\"message\" cols=\"50\" rows=\"7\" id=\"textarea_([0-9]+_[0-9]+)\"", curlData)
            userdata = re.findall(ur"firstinfo clearfix\">\n<strong><a href=\"\/n\/([^\"]+)\/\"", curlData)
            allcomments = re.findall(ur"<ul class=\"[0-9]+_[0-9]+\">(((?!<\/ul>)[\s\S])*)<\/ul>", curlData)

            triplets = zip(commentdata, userdata, [a for a,b in allcomments])

            for commentid, username, photocomments in triplets:
                tries = 0
                while 1:
                    if mode == "spam":
                        if username in seen:
                            print "User " + username + " already seen; skipping."
                            continue
                        else:
                            cur.execute("""INSERT INTO users (username) VALUES (%s);""", (username,))
                            con.commit()
                            seen.append(username)
                    posters = re.findall(ur"<a href=\"\/n\/([^\"]+)\/\"", photocomments)
                    if "famestapp" in posters:
                        print "Already posted on photo " + commentid + "; skipping."
                        continue
                    print "Posting comment on photo id " + commentid + "..."
                    # always quote user
                    # quote = '%40' + username
                    # 50% chances of quoting user at the beginning of comment
                    quote = '%40' + username + ' ' if random.randint(0, 1) == 1 else ''
                    message = comments[random.randint(0, len(comments) - 1)] if mode == "nospam" else spam_comments[random.randint(0, len(spam_comments) - 1)]
                    postdata = 'messageid=' + commentid + '&message=' + quote + message + '&t=' + str(random.randint(1000, 9999))
                    buf = cStringIO.StringIO()
                    c = pycurl.Curl()
                    c.setopt(pycurl.URL, "http://web.stagram.com/post_comment/")
                    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
                    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
                    c.setopt(pycurl.WRITEFUNCTION, buf.write)
                    c.setopt(pycurl.FOLLOWLOCATION, 1)
                    c.setopt(pycurl.ENCODING, "")
                    c.setopt(pycurl.SSL_VERIFYPEER, 0)
                    c.setopt(pycurl.SSL_VERIFYHOST, 0)
                    useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
                    c.setopt(pycurl.USERAGENT, useragent)
                    c.setopt(pycurl.POST, 1)
                    c.setopt(pycurl.POSTFIELDS, postdata)
                    c.setopt(pycurl.POSTFIELDSIZE, len(postdata))
                    c.perform()
                    response = buf.getvalue()
                    buf.close()
                    tries += 1
                    if re.match("\{\"status\":\"OK\",\"message\":\"Success.\"", response) != None:
                        commentcount += 1
                        hashtagcomments += 1
                        print "You commented on #" + tag + " image " + commentid + "! Comment count: " + str(commentcount)
                        if sleeptimer > 0:
                            time.sleep(sleeptimer)
                        break
                    else:
                        print "Try #" + str(tries) + " failed:" + response + "\nSleeping for one minute..."
                        time.sleep(60)
                        if tries == MAX_TRIES:
                            break
    con.close()

def like():
    likecount = 0
    sleepcount = 0
    for tag in hashtags:
        hashtaglikes = 0
        nextpage = "http://web.stagram.com/tag/"+tag+"/?vm=list"
        #enter hashtag like loop
        while nextpage != False and (hashtaglikelimit == 0 or (hashtaglikelimit > 0 and hashtaglikes < hashtaglikelimit)):
            buf = cStringIO.StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, nextpage)
            c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
            c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
            c.setopt(pycurl.WRITEFUNCTION, buf.write)
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            c.setopt(pycurl.ENCODING, "")
            c.setopt(pycurl.SSL_VERIFYPEER, 0)
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
            useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
            c.setopt(pycurl.USERAGENT, useragent)
            c.perform()
            curlData = buf.getvalue()
            buf.close()

            nextpagelink = re.findall(ur"<a href=\"([^\"]*)\" rel=\"next\">Earlier<\/a>",curlData)
            if len(nextpagelink)>0:
                nextpage = "http://web.stagram.com"+nextpagelink[0]
            else:
                nextpage = False

            likedata = re.findall(ur"<span class=\"like_button\" id=\"like_button_([^\"]*)\">",curlData)
            if len(likedata)>0:
                for imageid in likedata:
                    if hashtaglikelimit > 0 and hashtaglikes >= hashtaglikelimit:
                        break
                    repeat = True
                    while repeat:
                        randomint = random.randint(1000,9999)

                        postdata = 'pk='+imageid+'&t='+str(randomint)
                        buf = cStringIO.StringIO()
                        c = pycurl.Curl()
                        c.setopt(pycurl.URL, "http://web.stagram.com/do_like/")
                        c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
                        c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
                        c.setopt(pycurl.WRITEFUNCTION, buf.write)
                        c.setopt(pycurl.FOLLOWLOCATION, 1)
                        c.setopt(pycurl.ENCODING, "")
                        c.setopt(pycurl.SSL_VERIFYPEER, 0)
                        c.setopt(pycurl.SSL_VERIFYHOST, 0)
                        useragent = random.choice(browsers) + str(random.randrange(1,9)) + "." + str(random.randrange(0,50)) + " (" + random.choice(operatingsystems) + "; " + random.choice(operatingsystems) + "; rv:" + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + "." + str(random.randrange(1,9)) + ")"
                        c.setopt(pycurl.USERAGENT, useragent)
                        c.setopt(pycurl.POST, 1)
                        c.setopt(pycurl.POSTFIELDS, postdata)
                        c.setopt(pycurl.POSTFIELDSIZE, len(postdata))
                        #c.setopt(pycurl.VERBOSE, True)
                        c.perform()
                        postData = buf.getvalue()
                        buf.close()
                        if postData == '''{"status":"OK","message":"LIKED"}''':
                            likecount += 1
                            hashtaglikes += 1
                            print "You liked #"+tag+" image "+imageid+"! Like count: "+str(likecount)
                            repeat = False
                            sleepcount = 0
                            if sleeptimer > 0:
                                time.sleep(sleeptimer)
                        else:
                            sleepcount += 1
                            print "Your account has been rate limited. Sleeping on "+tag+" for "+str(sleepcount)+" minute(s). Liked "+str(likecount)+" photo(s)..."
                            time.sleep(60)

if __name__ == "__main__":
    if len(sys.argv) < 2 or (not (sys.argv[1] == "comment" and len(sys.argv) == 3 and (sys.argv[2] == "spam" or sys.argv[2] == "nospam")) and sys.argv[1] != "like"):
        print "Usage: python webstagrambot.py comment spam|nospam"
        print "Usage: python webstagrambot.py like"
    else:
        login()
        comment(sys.argv[2]) if sys.argv[1] == "comment" else like()
