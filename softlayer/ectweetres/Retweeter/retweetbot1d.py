# -*- coding: utf-8 -*-
import tweepy
import datetime
from elasticsearch import Elasticsearch
from datetime import timedelta
import sched, time
from random import randint

#Write info to the log file
def writeLog(msg):
    file_name = "log_retweetbot1d_0.dat"
    with open(file_name, "a") as myfile:
        myfile.write(msg + "\n")
    myfile.close()
s = sched.scheduler(time.time, time.sleep)
#DEVSBOTECU - 765271929657892864
#DA_GUZ - 496692665
def retweet_sched(sc):
        writeLog("Running retweeter...")
        es = Elasticsearch([{'host': '127.0.0.1', 'port': 9500}])
        tw_counter =0
        err_counter = 0
        follow_counter = 0
        # create bot DEVSBOTECU
        now = datetime.datetime.now()
        xminsago = datetime.datetime.now() - datetime.timedelta(hours=24)
        now=now - timedelta(hours=5)
        xminsago=xminsago- timedelta (hours=5)
        writeLog(unicode(now))
        auth = tweepy.OAuthHandler("HNSJ4IMIiqYvfk3Kt4gKeauSh", "m99K9Ic4hHurLWTMINO3a0oCY0TcRxx9nFq3K1z975VWbmg93L")
        auth.set_access_token("765271929657892864-uzxmR7hGokuAqzfB531zc4HdOpnjgVO", "ddvkb2rJ9tSHWOo9CACSARXZb7Jrn5jQPjrYPQfeqhkbc")
	api = tweepy.API(auth)
        res = es.search(index="ecuador-index", body={"sort":[{"retweeted_status.retweet_count":{"order":"desc"}}],"aggs":{"2":{"terms":{"field":"retweeted_status.user.screen_name","size":5},"aggs":{"1":{"max":{"field":"retweeted_status.retweet_count"}}}},"3":{"max":{"field":"retweeted_status.retweet_count"}}},"size":200,"query":{"filtered":{"query":{"query_string":{"analyze_wildcard":True,"query":"*"}},"filter":{"bool":{"must":[{"query":{"filtered":{"query":{"query_string":{"analyze_wildcard":True,"query":"*"}},"filter":{"range":{"retweeted_status.created_at":{"gte": xminsago,"lte": now,"time_zone": "-5:00"}}}}}}],"must_not":[]}}}}})
        writeLog("Got %d Hits:" % res['hits']['total'])
	tweetText = "Bip! Los twiteros más populares en las últimas 24 horas:\n"
	j=1
        for hit in res['aggregations']['2']['buckets']:
                try:
                        writeLog( hit["key"])
                        tweetText+=str(j)+".@"+str(hit["key"])+"\n"
                        tw_counter += 1
			j+=1
                except tweepy.error.TweepError as e:
                        # just in case tweet got deleted in the meantime or already retweeted
                        err_counter += 1
                        writeLog(str(e))
	writeLog(tweetText)
        try:    
                api.update_status(status=tweetText)
        except tweepy.error.TweepError as e:
                writeLog(str(e))
        writeLog("Finished. %d Tweets retweeted, %d errors occured." % (tw_counter, err_counter))
	sc.enter(86400, 1, retweet_sched, (sc,))
s.enter(200, 1, retweet_sched, (s,))
s.run()
