import urllib.request
import sys
import os

def main():
	if os.path.exists(sys.argv[2]):
		return
	resp = urllib.request.urlopen(sys.argv[1])
	with open(sys.argv[2], "wb") as f:
		f.write(resp.read())



if __name__ == "__main__":
	main()