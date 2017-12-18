# -*- coding: utf-8 -*-
import tweepy
import datetime
from elasticsearch import Elasticsearch
from datetime import timedelta
import sched, time
from random import randint

#Write info to the log file
def writeLog(msg):
    file_name = "log_retweetbot1welec_0.dat"
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
        xminsago = datetime.datetime.now() - datetime.timedelta(hours=168)
        now=now - timedelta(hours=5)
        xminsago=xminsago- timedelta (hours=5)
        writeLog(unicode(now))
        auth = tweepy.OAuthHandler("KHhIPqvhqfihoOiQxpg6oSFbL", "iXpqm5tkEESkiZAGerEEuiPLlBdXTqDrGfJHhUb2ZNa0KQsnWB")
        auth.set_access_token("765271929657892864-IToT3ieMDz9uI3sIhoPMfqAqBzKD8Hk", "9TBuWycoylX90wPL1rOFblMbSLjx4Hgaq1UZXfGD3D4EW")
        api = tweepy.API(auth)
        res = es.search(index="ecuador-index", body={"sort":[{"retweeted_status.retweet_count":{"order":"desc"}}],"aggs":{"2":{"terms":{"field":"retweeted_status.user.screen_name","size":5},"aggs":{"1":{"max":{"field":"retweeted_status.retweet_count"}}}},"3":{"max":{"field":"retweeted_status.retweet_count"}}},"size":200,"query":{"filtered":{"query":{"query_string":{"analyze_wildcard":True,"query":"*"}},"filter":{"bool":{"must":[{"query":{"filtered":{"query":{"query_string":{"analyze_wildcard":True,"fields" : ["retweeted_status.user.id"],"query":"760145761946497000 OR 375369761 OR 802207195572084000 OR 913131817 OR 315377387 OR 18661588 OR 24974978 OR 300390462"}},"filter":{"range":{"retweeted_status.created_at":{"gte": xminsago,"lte": now,"time_zone": "-5:00"}}}}}}],"must_not":[]}}}}})
        writeLog("Got %d Hits:" % res['hits']['total'])
	tweetText = "Bip! Los candidatos más retuiteados en la última semana:\n"
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
	api.update_status(status=tweetText)
        writeLog("Finished. %d Tweets retweeted, %d errors occured." % (tw_counter, err_counter))
	sc.enter(86400, 1, retweet_sched, (sc,))
s.enter(20, 1, retweet_sched, (s,))
s.run()
