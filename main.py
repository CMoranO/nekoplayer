import os
import subprocess
import requests
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.environ.get("DEBUG"):
    BASE_URL ="http://localhost:8001/ctrl/s/play/{}"
else:
    BASE_URL ="http://nekoanimedd.com/ctrl/s/play/{}"


def main(id):
    url = BASE_URL.format(id) 
    res = requests.get(url)
    url = res.content
    cmd = ["megadl", "'{}'".format(url), "--path","-","|", "mpv", "-"]
    print " ".join(cmd)
    subprocess.check_output(" ".join(cmd), shell=True)

if __name__ == "__main__":
    main(sys.argv[1])

