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
#    cmd = ['"{}\mega\megadl.exe"'.format(BASE_DIR), '"{}"'.format(url), "--path","-","|", '"{}\mpv\mpv.com"'.format(BASE_DIR), "-"]
    #cmd = ['"{}\mega\megadl.exe"'.format(BASE_DIR), '"{}"'.format(url), "--path","-","|", '"{}\mpv\mpv.com"'.format(BASE_DIR), "-"]
    
    mega_url = res.json().get("url","")
    version = res.json().get("version", -1)
    if VER != version:
        print cat
        print "Hay una version nueva!!! descargala"
        raw_input("adios ...")
        return
    
    cmd = ['"megadl"'.format(BASE_DIR), '"{}"'.format(mega_url), "--path","-","|", '"mpv"'.format(BASE_DIR), "-"]
    subprocess.check_output(" ".join(cmd), shell=True)


def start():
    main(sys.argv[1])

if __name__ == "__main__":
    start()




