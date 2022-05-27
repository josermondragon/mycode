#!/usr/bin/env python3


from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

app= Flask(__name__)

bodypartdata= [{
       "bodyPart":"neck",
       "equipment":"body weight",
       "gifUrl":"http://d205bpvrqc9yn1.cloudfront.net/1403.gif",
       "id":"1403",
       "name":"neck side strech",
       "target":"levator scapulae"
}] 

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           bodyPart=data["bodyPart"]
           equipment=data["equipment"]
           gifUrl=data["gifUrl"]
           id=data["id"]
           name=data["name"]
           target=data["target"]
           bodypartdata.append({"bodyPart":bodyPart,"equipment":equipment,"gifUrl":gifUrl,"id":id,"name":name,"target":target})
    # jsonify returns legal JSON
    return jsonify(bodypartdata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

