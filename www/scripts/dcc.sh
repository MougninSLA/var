#!/bin/bash

cd /usr/src
wget http://www.rhyolite.com/dcc/source/dcc.tar.Z
tar -zxvf dcc.tar.Z
cd dcc-1.3.120/
./configure && make && make install
cdcc info > /var/dcc/map.txt
chmod 0600 /var/dcc/map.txt
rm /var/dcc/map
cdcc "new map; load /var/dcc/map.txt"
cdcc "delete 127.0.0.1"