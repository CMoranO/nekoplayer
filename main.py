import os
import subprocess
import requests
import sys

BASE_DIR = os.path.dirname(sys.argv[0])

if os.environ.get("DEBUG"):
    BASE_URL ="http://localhost:8001/ctrl/s/play/{}"
else:
    BASE_URL ="http://nekoanimedd.com/ctrl/s/play/{}"

cat = """
		  \    /\
		   )  ( ')
		  (  /  )           Nekoanimedd Player
		   \(__)|
"""
	
	
def main(neko_id):
    _, id = neko_id.split(":")
    url = BASE_URL.format(id)
    res = requests.get(url)
    url = res.content
    cmd = ['"{}\mega\megadl.exe"'.format(BASE_DIR), '"{}"'.format(url), "--path","-","|", '"{}\mpv\mpv.com"'.format(BASE_DIR), "-" , ""]
    #print " ".join(cmd)+
	print cat
    subprocess.check_output(" ".join(cmd), shell=True)

if __name__ == "__main__":
    main(sys.argv[1])




