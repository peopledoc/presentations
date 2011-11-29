import urllib
import json
import sys

print json.load(urllib.urlopen("http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=%s" % (sys.argv[1], 1)))[0]['text']