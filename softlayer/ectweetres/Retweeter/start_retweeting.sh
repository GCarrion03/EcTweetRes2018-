#!/bin/bash
# A script which starts the retweet process
# Authors: Gustavo Carrion
if [ $# -lt 2 ]
  then
    nohup python retweetbot.py & nohup python retweetbot6h.py & nohup python retweetbot1d.py nohup python retweetbot6helec.py & nohup python retweetbot1delec.py & nohup python retweetbot1welec.py
fi

eval "./check_process.sh &"
