set -e
MPVARCH='i686'
MEGAARCH='win32'
DATE='20160118'
VER1='1.9.97'
VER='1.9.97'
rm -rf dist
#python setup.py py2exe
pyinstaller -i cat.ico -F  main.py

wget -c  https://mpv.srsfckn.biz/mpv-$MPVARCH-$DATE.7z -O mpv.7z
7z x mpv.7z  -odist/mpv/ -y
rm dist/mpv/*.pdf

wget -c https://megatools.megous.com/builds/megatools-$VER1-$MEGAARCH.zip -O mega.zip
7z x mega.zip -odist/mega/ -y
mv -f dist/mega/megatools-$VER-$MEGAARCH/* dist/mega/
rm dist/mega/megatools-$VER-$MEGAARCH/ -rf

chmod +x -R dist