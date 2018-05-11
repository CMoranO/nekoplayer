SET MPVARCH=i686
SET MEGAARCH=win32
SET DATE=20171225
SET VER=1.9.98
del /Q dist

pyinstaller -i cat.ico -F  main.py

python download.py https://mpv.srsfckn.biz/mpv-%MPVARCH%-%DATE%.7z mpv.7z
7z x mpv.7z  -odist/mpv/ -y
del dist\mpv\*.pdf /Q /F /S

python download.py https://megatools.megous.com/builds/megatools-%VER%-%MEGAARCH%.zip  mega.zip
7z x mega.zip -odist/mega/ -y
move  dist\mega\megatools-%VER%-%MEGAARCH%\* dist\mega\
del /Q /F /S dist\mega\megatools-%VER%-%MEGAARCH%\


copy  dist\mega mega 
copy  dist\mpv mpv 
compil32 /cc setup.iss