#!/usr/bin/python
# coding: utf-8
# Python program to dump the playlist from doubanfm.
# And play it with mpg321
# The channel id can be obtabined by http://douban.fm/j/explore/channel_detail?channel_id=101
# 1: 华语, 2: 欧美, 3: 七零, 4: 八零, 5: 九零, 6: 粤语, 7: 摇滚, 8: 民谣, 9: 轻音乐, 10: 电影原声
# 2015 @Samue Hsu

import httplib
import json
import os
import sys
import subprocess
import time

reload(sys)
sys.setdefaultencoding('utf-8')

while True:
    # connect to doubanfm web server
    httpConnection = httplib.HTTPConnection('douban.fm')
    httpConnection.request('GET', '/j/mine/playlist?type=n&channel=10')
    song = json.loads(httpConnection.getresponse().read())['song']

    # dump the required field and play it with mpg321
    for curr_song in song:
       print "Title: " + curr_song['title'] + "\tDuration: " +  str(curr_song['length']) + " seconds"
       # print curr_song['url']
       mpd_cmd = subprocess.Popen(['mpg321', curr_song['url']])
       mpd_cmd.wait()
