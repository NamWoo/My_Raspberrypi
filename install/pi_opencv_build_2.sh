#!/bin/bash

time sudo make -j4

sudo make install
sudo ldconfig

sudo sed -i "s/CONF_SWAPSIZE=2048/CONF_SWAPSIZE=100/g" /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile restart

free