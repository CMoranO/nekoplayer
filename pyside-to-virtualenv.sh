#!/bin/bash
# Symlinks PySide from global installation into virtualenv site-packages

platform='unknown'
unamestr=$(uname)
if [[ "$unamestr" == 'Linux' ]]; then
    platform='linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
    platform='darwin'
fi

LIBS=( PySide pysideuic )

PYTHON_VERSION=python$(python -c "import sys; print (str(sys.version_info[0])+'.'+str(sys.version_info[1]))")
VAR=( $(which -a $PYTHON_VERSION) )

GET_PYTHON_LIB_CMD="from distutils.sysconfig import get_python_lib; print (get_python_lib())"
LIB_VIRTUALENV_PATH=$(python -c "$GET_PYTHON_LIB_CMD")

if [[ $platform == 'linux' ]]; then
    LIB_SYSTEM_PATH=$(${VAR[-1]} -c "$GET_PYTHON_LIB_CMD")
elif [[ $platform == 'darwin' ]]; then
    LIB_SYSTEM_PATH=$(/opt/local/bin/python2.7 -c "$GET_PYTHON_LIB_CMD")
else
    echo "unsupported platform; not doing symlinks"
fi

for LIB in ${LIBS[@]}
do
    if [[ ! -e $LIB_VIRTUALENV_PATH/$LIB ]]; then
        ln -s $LIB_SYSTEM_PATH/$LIB $LIB_VIRTUALENV_PATH/$LIB
    fi
done
