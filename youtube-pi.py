#!/usr/bin/python

import sys
import subprocess
import urllib
import requests
import json
import random
import pprint
import time
import os
import os.path

channelId = "UCceEPxhcejQiYza8bvuAA8g" # Eco-Virtual
#channelId = "UCpclRlEJ2oh6JDEJy68UjKA" # an0nymooose
#channelId = "UCzNZlJzmjomyl00ewlxHqOA" # Cool3DWorld
#channelId = "UCYfArGrC66A-vdS45DS7Qrg" # Ace's Adventures

directory = "videos"

if not os.path.exists(directory):
    os.makedirs(directory)

pp = pprint.PrettyPrinter(indent=4)
videos = []
YOUTUBE_DATA_API_KEY = os.environ['YOUTUBE_DATA_API_KEY']

def populate():
	query = {"channelId": channelId, "maxResults": 50, "part": "snippet,id", "key": YOUTUBE_DATA_API_KEY, "order": "date"};
	feed_url = "https://www.googleapis.com/youtube/v3/search?" + urllib.urlencode(query)
	r = requests.get(feed_url)
	doc = json.loads(r.text)
	num_items = len(doc["items"]) 
	
	for item in doc["items"]:
		if "videoId" in item["id"]:
			video = {"id": item["id"]["videoId"], "title": item["snippet"]["title"]}
			pp.pprint( video )
			videos.append( video )
	return

def get_video():
	video = random.choice(videos)
	video_url = "http://www.youtube.com/watch?v=" + video["id"]
	path = "%s/%s.mp4" % (directory, video["id"])
	if os.path.isfile(path):
		return path

	print "Downloading {0} to {1}".format(video_url, path)
	cmd = ['youtube-dl', '-f', '18', '--output', 'videos/%(id)s.%(ext)s', video_url]
	yt = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(res,err) = yt.communicate()
	
	if err:
		print(err)
		return None

	if not os.path.isfile(path):
		print "Error while downloading... {0} not found".format(path)
		return None

	return path


		


def play_video():
	path = get_video()
	if(path is not None):
		print "Playing {0}".format(path)
		cmd = ['omxplayer', '-b', path]
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(res,err) = p.communicate()
	else:
		print("Got a bad video. Sleeping.")
		time.sleep( 1 )

def main(argv):
	populate()

	while True:
		play_video()

if __name__ == "__main__":
   main(sys.argv[1:])
