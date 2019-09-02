#Converting python as binary
#cython -2 --embed -o nc_json2xml.c nc_json2xml.py
#gcc -v -Os -I  /usr/include/python2.7 -lpython2.7 nc_json2xml.c -o nc_json2xml

import json
import sys
import urllib
import dicttoxml
filename = sys.argv[1]
page = urllib.urlopen(filename)
content = page.read()
obj = json.loads(content)
xml = dicttoxml.dicttoxml(obj)
f = open(filename[0:-5]+".xml", "w")
f.write(xml)
f.close()

# compiling 
#python json2xml.py test.json
