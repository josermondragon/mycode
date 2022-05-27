#!/usr/bin/env python3
import requests
from pprint import pprint
import json

URL= "http://127.0.0.1:2224/trainer"

new_bodyPart = {
                "bodyPart":"neck",
                "equipment":"body weight",
                "gifUrl":"http://d205bpvrqc9yn1.cloudfront.net/0716.gif",
                "id":"0716",
                "name":"side push neck stretch",
                "target":"levator scapulae"
               }

#json to python
new_bodyPart= json.dumps(new_bodyPart)

#request.post
resp= requests.post(URL,json=new_bodyPart)

#pretty print
pprint(resp)

