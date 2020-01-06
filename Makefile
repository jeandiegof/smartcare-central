install:
	sudo apt install bluetooth libbluetooth-dev python3-pip
	pip3 install pybluez
	# gattlib
	sudo apt install libglib2.0-dev libboost-all-dev
	pip3 download gattlib
	tar xvzf ./gattlib-0.20150805.tar.gz
	cd gattlib-0.20150805/
	sed -ie 's/boost_python-py34/boost_python37/' setup.py
	pip3 install .
