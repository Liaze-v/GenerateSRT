import os
import json
import textwrap
import deepl
import time
import requests


def jsoncreate(filename):
    # Opening JSON file
    fjson = open(filename)
    data = json.load(fjson)
    lines = []
    for segment in data["segments"]:
        original_string = segment["text"]
        trimmed_string = original_string.strip()
        lines.append([trimmed_string])
        # lines.append([packedText(segment["text"])])
    with open("{}.text".format(filename.removesuffix('.json')), "w", encoding="utf-8") as f:
        for line in lines:
            for l in line:
                f.write(l)
                # f.write('\n')
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
    if not os.path.exists("{}.text".format(namefile.removesuffix(endsuffix))):
        jsoncreate(namefile)

# filename = "nameofjson.json"
# jsoncreate("nameofjson.json")

