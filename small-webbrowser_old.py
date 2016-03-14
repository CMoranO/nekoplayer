#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import QObject, Slot
from PySide.QtGui import QApplication
from PySide.QtWebKit import QWebView
import os
import subprocess
import requests
import sys
import webbrowser
#from guessit import guessit
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


html = """
<html>
<body>
    <h1>Hello!</h1><br>
    <h2><a href="#" onclick="printer.text('%s')">Play %s</a></h2>

</body>
</html>
""" % ( sys.argv[1], sys.argv[1])



def neko(neko_id):
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


    mega_path = os.path.join(BASE_DIR, 'mega', 'megadl.exe')
    mpv_path = os.path.join(BASE_DIR, "mpv","mpv.com")
    cmd = ['"{}"'.format(mega_path), '"{}"'.format(mega_url),
           "--path","-","|",
           '"{}"'.format(mpv_path), "-" , '--no-terminal']
           #'--fullscreen']
    print "Cargando...."
    #webbrowser.open("http://bc.vc/QODvAp")
    subprocess.check_output(" ".join(cmd), shell=True)

class ConsolePrinter(QObject):
    def __init__(self, parent=None):
        super(ConsolePrinter, self).__init__(parent)

    @Slot(str)
    def text(self, message):
        neko(message)
        print message

def main():
    app = QApplication(sys.argv)
    view = QWebView()
    frame = view.page().mainFrame()
    printer = ConsolePrinter()

    view.setHtml(html)
    frame.addToJavaScriptWindowObject('printer', printer)
    #frame.evaluateJavaScript("alert('Hello');")
    #frame.evaluateJavaScript("printer.text('Goooooooooo!');")
    view.show()

    app.exec_()


if __name__ == '__main__':
    main()
