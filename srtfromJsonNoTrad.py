import os
import json
import textwrap
import deepl
import time
import requests




def timecode(number):
    if number > 3600:
        hours = int(number // (60 * 60))
    else:
        hours = 0
    minutes = int(number // 60)
    secondes = number - (minutes * 60)
    # milisecondes = number - int(number)
    milisecondesStr = str(number-int(number)).split('.')[1]
    milisecondes = int(milisecondesStr[0:3])
    return hours, minutes, secondes, milisecondes


def create_timecode(number1, number2):
    timer = r"%02d:%02d:%02d,%03d" % (timecode(number1)) +" --> "+ r"%02d:%02d:%02d,%03d" % (timecode(number2))
    return timer


def jsoncreate(filename):
    # Opening JSON file
    fjson = open(filename)
    data = json.load(fjson)
    lines = []
    for segment in data["segments"]:
        lines.append([str(segment["id"]+1), create_timecode(segment["start"],segment["end"]), segment["text"]])
        # lines.append([packedText(segment["text"])])
    with open("{} - [Original].srt".format(filename.removesuffix('.json')), "w", encoding="utf-8") as f:
        for line in lines:
            for l in line:
                f.write(l)
                f.write('\n')
            f.write('\n')
            
def listOFFiles():
    filesToGenerate = []
    for root, dirs, files in os.walk("./videofile", topdown=False):
        for name in files:
                if name.endswith(('.json')):
                    print(os.path.join(root, name))
                    filesToGenerate.append(os.path.join(root, name))
        #    for name in dirs:
        #       print(os.path.join(root, name))
    print(filesToGenerate)
    return filesToGenerate


nameAllFile = listOFFiles()
for namefile in nameAllFile:
    endsuffix = ""
    for suffix in ('.json'):
        if namefile.endswith(suffix):
            endsuffix = suffix
    if not os.path.exists("{} - [Original].srt".format(namefile.removesuffix(endsuffix))):
        jsoncreate(namefile)

# filename = "nameofjson.json"
# jsoncreate("nameofjson.json")

