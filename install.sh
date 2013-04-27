#!/bin/bash

set -e

mkdir -p ~/.src
curl https://raw.github.com/brigand/src/master/src.py > ~/.src/src.py
chmod a+x ~/.src/src.py
cd /usr/sbin
ln -s ~/.src/src.py src
