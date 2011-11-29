import urllib
import json
import sys

print "Last %s tweets:" % sys.argv[2]

for tweet in json.load(urllib.urlopen("http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=%s" % (sys.argv[1], sys.argv[2]))):
	print tweet['text']