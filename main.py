import os
import subprocess
import requests
import sys
from gooey import Gooey, GooeyParser

BASE_DIR = os.path.dirname(sys.argv[0])

if os.environ.get("DEBUG"):
    BASE_URL ="http://localhost:8001/ctrl/s/play/{}"
else:
    BASE_URL ="http://nekoanimedd.com/ctrl/s/play/{}"
	

def main(neko_id):
    _, id = neko_id.split(":")
    url = BASE_URL.format(id)
    res = requests.get(url)
    url = res.content
    mega_path = os.path.join(BASE_DIR, 'mega', 'megadl.exe')
    mpv_path = os.path.join(BASE_DIR, "mpv","mpv.com")
    cmd = ['"{}"'.format(mega_path), '"{}"'.format(url),
           "--path","-","|",
           '"{}"'.format(mpv_path), "-"
           ]
    print " ".join(cmd)
    subprocess.check_output(" ".join(cmd), shell=True)

@Gooey()
def start():
    main(sys.argv[1])

if __name__ == "__main__":
    start()




