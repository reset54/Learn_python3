
#!/bin/bash

# variables


# go to the folder whert we make work-directory, with the USER_NAME (reset54)
cd /home/reset54/

# update the package manager dependencies
sudo apt update && sudo apt upgrade

# install the necessary libraries to install and build 
# python 3.10.0 from source
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Download the archive, with Python
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz

# Extract the archive
tar -xzvf Python-3.10.0.tgz

# Navigate to the extracted directory
cd Python-3.10.0

# run the configure command to see if the necessary dependencies are available. 
# command uses the -enable-optimizations flag to optimize the binary and run multiple tests.
./configure --enable-optimizations --prefix=/home/reset54/.python3.10/

# startup assembly, number of processor cores on the server (6)
make -j 6 

# install python into /home/reset54/.python3.10/
# altinstall flag is used to save the default Python binary path in /usr/bin/python.
sudo make altinstall

# remove arvhive tar.gz and dir Python-3.10.0
cd /home/reset54/
sudo rm -rf Python-3.10.0*

# add our python in PATH (bash.rc - file)
# sudo cat "export PATH=$PATH:/home/reset54/.python3.10/bin" >> ~/.bashrc

# run bashrc file
# source ~/.bashrc

# check the python version, was the installation successful?
# python3.10 --version
