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


def packedText(text):
    text = text.lstrip()
    #----Deepl API----
    # auth_key = ""
    # translator = deepl.Translator(auth_key)
    # result = translator.translate_text(text, target_lang="FR")
    # text = result.text
    #----Deepl API----
    #----libretranslate API----
    url = 'http://127.0.0.1:5000/translate'
    myobj = {
        'q': text,
        'source': 'en',
        'target': 'fr',
        'format': 'text'
        }
    resultlibre = requests.post(url, json = myobj)
    textforjson = resultlibre.text
    texttojson = json.loads(textforjson)
    text = texttojson["translatedText"]
    print(text)
    #----libretranslate API----
    if len(text) > 42:
        textwraped = textwrap.wrap(text,42)
        if len(textwraped) > 3:
            textpacked = textwraped[0]+"\n"+textwraped[1]+" "+textwraped[2]+" "+textwraped[3]
        elif len(textwraped) > 2:
            textpacked = textwraped[0]+"\n"+textwraped[1]+" "+textwraped[2]
        else:
            textpacked = textwraped[0]+"\n"+textwraped[1]
    else:
        textpacked = text
    return textpacked


def jsoncreate(filename):
    # Opening JSON file
    fjson = open(filename)
    data = json.load(fjson)
    lines = []
    for segment in data["segments"]:
        lines.append([str(segment["id"]+1), create_timecode(segment["start"],segment["end"]), packedText(segment["text"])])
        #----Deepl API----
        time.sleep(0.5)
        #----Deepl API----
    # with open("{} - [libretranslate] - French.srt ".format(filename.removesuffix('.json')), "w", encoding="utf-8") as f:
    with open("{} - [libretranslate] - English.srt ".format(filename.removesuffix('.json')), "w", encoding="utf-8") as f:
        for line in lines:
            for l in line:
                f.write(l)
                f.write('\n')
            f.write('\n')
            
            
# filename = "nameofjson.json"
# jsoncreate(filename)

