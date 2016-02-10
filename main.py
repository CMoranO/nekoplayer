import os
import subprocess
import requests
import sys

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
       \(__)|  
""" % VER
	
	

def main(neko_id):
    _, id = neko_id.split(":")
    url = BASE_URL.format(id)
    res = requests.get(url)
    mega_url = res.json().get("url")
    version = res.json().get("version", -1)
    if VER != version:
        print cat
        print "Hay una version nueva!!! descargala"
        raw_input("adios ...")
        return 
    mega_path = os.path.join(BASE_DIR, 'mega', 'megadl.exe')
    mpv_path = os.path.join(BASE_DIR, "mpv","mpv.com")
    cmd = ['"{}"'.format(mega_path), '"{}"'.format(mega_url),
           "--path","-","|",
           '"{}"'.format(mpv_path), "-" , '--quiet'
           ]
    print " ".join(cmd)
    subprocess.check_output(" ".join(cmd), shell=True)


def start():
    main(sys.argv[1])

if __name__ == "__main__":
    start()




