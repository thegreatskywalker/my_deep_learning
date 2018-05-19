# This script is designed to work with ubuntu 16.04 LTS

# ensure system is updated and has basic build tools
sudo apt-get update
sudo apt-get --assume-yes upgrade
sudo apt-get --assume-yes install tmux build-essential gcc g++ make binutils
sudo apt-get --assume-yes install software-properties-common

# make downloads directory
cd ~
mkdir downloads
cd downloads

# install Anaconda for current user
wget "https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh" -O "Anaconda3-5.0.1-Linux-x86_64.sh"
bash "Anaconda3-5.0.1-Linux-x86_64.sh" -b
source ~/.bashrc

echo "export PATH=\"$HOME/anaconda3/bin:\$PATH\"" >> ~/.bashrc
export PATH="$HOME/anaconda3/bin:$PATH"
conda install -y bcolz
conda upgrade -y --all
source ~/.bashrc

# setup Anaconda enviornment
echo "Setting up Anaconda enviornment for Algorithmica"
wget https://raw.githubusercontent.com/thegreatskywalker/my_deep_learning/master/Anaconda_Setup/linux_tensorflow_gpu.yml
#conda env create -f linux_tensorflow_gpu.yml 
conda env create -f linux_tensorflow_cpu.yml -n tensorflow_cpu

# clone the Algoritmica course repo and prompt to start notebook
cd ~
git clone https://github.com/algorithmica-repository/deep-learning
echo "\"jupyter notebook\" will start Jupyter on port 8888"
echo "If you get an error instead, try restarting your session so your $PATH is updated"

# install aria for parallel downloads
sudo apt install aria2
