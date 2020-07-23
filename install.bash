#!/usr/bin/bash

she() { 
echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

[ -d ~/.local/bin ] || { mkdir ~/.local ;  mkdir ~/.local/bin ; }

cp sten.py ~/.local/bin/sten &&

cd ~/.local/bin &&

python3 -m venv sten-venv &&

sten-venv/bin/pip install --upgrade pip &&

sten-venv/bin/pip install Pillow &&

abspath=$(she sten-venv/bin/python3) &&

echo "#!$(echo "$abspath" )" | cat - sten > temp && mv temp sten &&

chmod u+r+x sten && 

cd - &&

cat addtopath.txt

