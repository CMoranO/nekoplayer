#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import platform as _platform
from PySide.QtCore import QObject, Slot, QThread, QProcess
from PySide.QtCore import QCoreApplication
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

pid=None

def neko(neko_id='neko:v2Yr'):
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
    p1 = QProcess()
    p2 = QProcess()
    p1.setStandardOutputProcess(p2)
    p1.start('{}'.format(mega_path), ['{}'.format(mega_url),"--path","-"])
    p2.start('{}'.format(mpv_path), ["-" , '--no-terminal'])
    p2.waitForFinished()
    #print p2.readAll()
#           "--path","-",)
    #cmd = ['"{}"'.format(mega_path), '"{}"'.format(mega_url),
#           "--path","-","|",
#           '"{}"'.format(mpv_path), "-" , '--no-terminal']
           #'--fullscreen']
    print "Cargando...."
    #webbrowser.open("http://bc.vc/QODvAp")
    #pid = subprocess.call(" ".join(cmd), shell=True)

class ConsolePrinter(QObject):
    def __init__(self, parent=None):
        super(ConsolePrinter, self).__init__(parent)

    @Slot(str)
    def text(self, message):
        print ">",message
        neko(message)

        #print message

class OpenThread(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)

    def run(self):
        neko()




def main():
    app = QApplication(sys.argv)
    view = QWebView()
    frame = view.page().mainFrame()
    printer = ConsolePrinter()

    view.setHtml(html)
    frame.addToJavaScriptWindowObject('printer', printer)
    frame = frame
    #frame.evaluateJavaScript("alert('Hello');")
    #frame.evaluateJavaScript("printer.text('Goooooooooo!');")
    view.show()
    app.processEvents()
    app.exec_()


if __name__ == '__main__':
    main()
