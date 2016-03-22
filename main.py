import os
import subprocess
import requests
import sys
import webbrowser
#from guessit import guessit
from sys import platform as _platform

VER=1

BASE_DIR = os.path.dirname(sys.argv[0])

if os.environ.get("DEBUG"):
    BASE_URL ="http://localhost:8001/ctrl/s/play/{}"
else:
    BASE_URL ="http://nekoanimedd.com/ctrl/s/play/{}"

cat ="""
     \    /\\
      )  ( ')
      (  /  )    NekoplayerDD (beta) v%s
       \(__)|    http://www.nekoanimedd.com
""" % VER



def main(neko_id):
    _, id = neko_id.split(":")

    url = BASE_URL.format(id)
    res = requests.get(url)

    mega_url = res.json().get("url","")
    version = res.json().get("version", -1)

    if VER != version:
        print cat
        print "Hay una version nueva!!! descargala"
        raw_input("adios ...")
        return

    print cat

    if _platform == "linux" or _platform == "linux2":
        mega_path = "megadl"
        mpv_path = "mpv"
    elif _platform == "darwin":
              # MAC OS X
        pass
    elif _platform == "win32":
                 # Windows
        mega_path = os.path.join(BASE_DIR, 'mega', 'megadl.exe')
        mpv_path = os.path.join(BASE_DIR, "mpv","mpv.com")
    cmd = ['"{}"'.format(mega_path), '"{}"'.format(mega_url),
           "--path","-","|",
           '"{}"'.format(mpv_path), "-" , '--fullscreen','--cache=1024',
           '--no-terminal'
           ]
    print "Cargando...."
    #webbrowser.open("http://bc.vc/QODvAp")
    subprocess.check_output(" ".join(cmd), shell=True)

def start():
    main(sys.argv[1])

if __name__ == "__main__":
    start()
