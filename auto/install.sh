#!/bin/bash
INSTALLDIR=$PWD

# add PPA reps
#add-apt-repository ppa:nilarimogard/webupd8 --yes
#add-apt-repository ppa:gijzelaar/snap7 --yes

apt update && apt upgrade

# Libs and other softwares
apt install -y  p7zip \
		python3-pip \
            	python3-setuptools \
		python3-tk \
	    	jupyter-notebook \
            	git \
		libgtk-3-dev \
		libjpeg-dev \
		libtiff-dev  \
		libsdl1.2-dev \
		libgstreamer1.0-dev \
		libgstreamer-plugins-base1.0-dev \
		libnotify-dev \
		freeglut3 \
		freeglut3-dev \
		libsm-dev \
		libwebkitgtk-dev \
		libwebkitgtk-3.0-dev \


# libsnap7

wget -q https://downloads.sourceforge.net/project/snap7/1.4.2/snap7-full-1.4.2.7z
7z x snap7-full-1.4.2.7z
cd $INSTALLDIR/snap7-full-1.4.2/build/unix
make -f $INSTALLDIR/snap7-full-1.4.2/build/unix/x86_64_linux.mk
cd $INSTALLDIR

# Pip packages
pip3 install -r $INSTALLDIR/pip_packages.txt

# Gooey
pip3 install https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04/wxPython-4.0.0b1-cp36-cp36m-linux_x86_64.whl
git clone https://github.com/chriskiehl/Gooey.git
pip3 install -r $INSTALLDIR/Gooey/requirements.txt
python3 $INSTALLDIR/Gooey/setup.py install
# Workarround for Gooey libpng12
wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
dpkg -i /tmp/libpng12.deb
rm /tmp/libpng12.deb

# Pylon installation
# cd ~/pylon-5.1.0.12682-x86_64
tar -C /opt -xzf $INSTALLDIR/pylonSDK*.tar.gz
$INSTALLDIR/setup-usb.sh
# cd /usr/bin
ln -s /opt/pylon5/bin/PylonViewerApp /usr/bin/PylonViewerApp


# PyPylon
wget -O -q /tmp/pypylon.whl https://github.com/basler/pypylon/releases/download/1.3.1/pypylon-1.3.1-cp36-cp36m-linux_x86_64.whl
pip3 install /tmp/pypylon.whl
rm /tmp/pypylon.whl -f
