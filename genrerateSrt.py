import os
import whisper
import json
from translate import jsoncreate
import requests
import time

# First python to launch


def listOFFiles():
    filesToGenerate = []
    for root, dirs, files in os.walk("./videofile", topdown=False):
        for name in files:
                if name.endswith(('.mp3', '.mp4','.ts','.mkv')):
                    print(os.path.join(root, name))
                    filesToGenerate.append(os.path.join(root, name))
        #    for name in dirs:
        #       print(os.path.join(root, name))
    print(filesToGenerate)
    return filesToGenerate

def generateSrtdef(namefile,endsuffix):
    model = whisper.load_model("base")
    name = namefile
    result = model.transcribe(name,fp16=False,language='en')
    # os.system("whisper 'video.mp4' --language en --model tiny --Fp16 False")
    # name2= f"{name}"
    # newPath = name2.replace(os.sep, '/')
    # result = os.system('whisper "'+newPath+'" --language ru --model tiny')
    with open("{}.json ".format(namefile.removesuffix(endsuffix)), "w") as f:
        # json.dump(result, f)
        json.dump(result, f)

nameAllFile = listOFFiles()
for namefile in nameAllFile:
    endsuffix = ""
    for suffix in ('.mp3', '.mp4','.ts','.mkv'):
        if namefile.endswith(suffix):
            endsuffix = suffix
    if not os.path.exists("{}.json".format(namefile.removesuffix(endsuffix))):
        generateSrtdef(namefile,endsuffix)
    # if not os.path.exists("{} - [libretranslate] - French.srt".format(namefile.removesuffix('.mp4'))):
    if not os.path.exists("{} - [libretranslate] - English.srt".format(namefile.removesuffix('.mp4'))):
        jsoncreate(namefile.removesuffix(endsuffix)+".json")







