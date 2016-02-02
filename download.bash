ARCH='i686'
DATE='20160118'
VER1='1-9.96'
VER='1.9.96'

python setup.py py2exe

wget -c  https://mpv.srsfckn.biz/mpv-$ARCH-$DATE.7z -O mpv.7z
7z x mpv.7z  -odist/mpv/ -y
rm dist/mpv/*.pdf

wget -c https://megatools.megous.com/builds/megatools-$VER1-win32.zip -O mega.zip
7z x mega.zip -odist/mega/ -y
mv dist/mega/megatools-$VER-win32/* dist/mega/
rm dist/mega/megatools-$VER-win32/ -rf