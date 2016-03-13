SET MPVARCH=i686
SET MEGAARCH=win32
SET DATE=20160118
SET VER1=1.9.97
SET VER=1.9.97
rm -rf dist

pyinstaller -i cat.ico -F  main.py

wget -c  https://mpv.srsfckn.biz/mpv-%MPVARCH%-%DATE%.7z -O mpv.7z
7z x mpv.7z  -odist/mpv/ -y
rm dist/mpv/*.pdf

wget -c https://megatools.megous.com/builds/megatools-%VER1%-%MEGAARCH%.zip -O mega.zip
7z x mega.zip -odist/mega/ -y
mv -f dist/mega/megatools-%VER%-%MEGAARCH%/* dist/mega/
rm dist/mega/megatools-%VER%-%MEGAARCH%/ -rf

chmod +x -R dist

cp dist/mega mega -rf
cp dist/mpv mpv -rf