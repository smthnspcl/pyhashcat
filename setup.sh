#!/usr/bin/bash

sudo apt install -y git build-essential python3 python3-dev > /dev/null 2>&1

if [ ! -d "hashcat" ]; then
  echo "initializing and updating submodules"
  git submodule update --init > /dev/null 2>&1
  sed -i "1s/^/#include <deps\/zlib\/zconf.h>\n/" hashcat/deps/zlib/contrib/minizip/crypt.h
else
  echo "hashcat directory exists; not pulling"
fi

cd hashcat
HCL=$(find /usr/local/lib -name 'libhashcat*' | head -n 1)
if [ "$HCL" == "" ]; then
  echo "installing the hashcat library"
  sudo make -j4 install_library > /dev/null 2>&1
else
  echo "libhashcat is already installed"
fi

HCP=$(find /usr/bin -name 'hashcat' | head -n 1)
if [ "$HCP" == "" ]; then
  echo "installing hashcat itself"
  sudo make -j4 install > /dev/null 2>&1
else
  echo "hashcat is already installed"
fi

cd ..

HCLD="/usr/lib/libhashcat.so"
if [ ! -f "$HCLD" ]; then
  echo "no $HCLD; softlinking it"
  HCL=$(find /usr/local/lib -name 'libhashcat*' | head -n 1)
  sudo ln -s "$HCL" "$HCLD"
else
  echo "$HCLD already exists; no need for a soft link"
fi

echo "leaving hashcat here, if you need space remove it yourself"

echo "building pyhashcat"
python3 setup.py build > /dev/null 2>&1
echo "installing pyhashcat"
sudo python3 setup.py install > /dev/null 2>&1
echo "done"