<br/>
<p align="center">
  <h3 align="center">GenerateSRT</h3>

  <p align="center">
    generate translated subtitle of a bunch of videos
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)

## About The Project

The purpose of this project is to create automatically translated subtitles for several videos in succession.

Ideal for follow a courses in another language

## Built With

Python 3.9

## Getting Started

Add you vidéo file in to "videofile"  directory

### Prerequisites

If you use DEEPL, you have to get api key

Otherwise
You need to have install the project libretanslate (open source translation). And makesure you can acces it in terminal

### Installation

Download the repo
```sh
git clone https://github.com/Liaze-v/GenerateSRT.git
```

Then create a venv
```sh
python -m venv venv
```

Activate it
```sh
.venv\Scripts\activate
```
Dependencies

```sh
pip install deepl
```
```sh
pip install requests
```
```sh
pip install time
```
```sh
pip install textwrap
```
```sh
pip install json
```

## Usage

Then paste your videos in the zae directory.

Translation with Libtranslate
Launch 
```sh
Libtranslate.bat
```


Then in another terminal Run 
```sh
python genrerateSrt.py
```

Translation with DEEPL:
Go to "translate.py"
Comment between ----libretranslate API----
And uncomment between ----Deepl API----

Finally add your api key
auth_key = ""
Then run 
```sh
python genrerateSrt.py
```

The code is currently written to translate and generate French subtitles from English.

If your videos are not in English, go to the file "genrerateSrt.py"
Then modify the "generateSrtdef" function 


```sh
model.transcribe(name,fp16=False,language='en')
```

For a target language other than French,
Go to the file and change "target_lang" to DEEPL or "target" to Libtranslate
