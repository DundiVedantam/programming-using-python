#Converting all JSON files to XML files in a folder 
from glob import glob
import json
import urllib
import os
import dicttoxml
json_dir_name = 'data/*.json'
for f_name in glob(json_dir_name):
    if os.path.getsize(f_name) > 0:
       page = urllib.urlopen(f_name)
       content = page.read()
       obj = json.loads(content)
       xml = dicttoxml.dicttoxml(obj)
       f = open(f_name[0:-5]+".xml", "w")
       f.write(xml)
       f.close()
