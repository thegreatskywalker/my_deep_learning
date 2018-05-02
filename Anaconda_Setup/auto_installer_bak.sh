# This script is designed to work with ubuntu 16.04 LTS

# ensure system is updated and has basic build tools
sudo apt-get update
sudo apt-get --assume-yes upgrade
sudo apt-get --assume-yes install tmux build-essential gcc g++ make binutils
sudo apt-get --assume-yes install software-properties-common

# download and install GPU drivers
wget "http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.44-1_amd64.deb" -O "cuda-repo-ubuntu1604_8.0.44-1_amd64.deb"

sudo dpkg -i cuda-repo-ubuntu1604_8.0.44-1_amd64.deb
sudo apt-get update
sudo apt-get -y install cuda
sudo modprobe nvidia
nvidia-smi

# install cudnn libraries
wget "http://files.fast.ai/files/cudnn.tgz" -O "cudnn.tgz"
tar -zxf cudnn.tgz
cd cuda
sudo cp lib64/* /usr/local/cuda/lib64/
sudo cp include/* /usr/local/cuda/include/

# install Anaconda for current user
mkdir downloads
cd downloads
wget "https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh" -O "Anaconda3-5.0.1-Linux-x86_64.sh"
bash "Anaconda3-5.0.1-Linux-x86_64.sh" -b

echo "export PATH=\"$HOME/anaconda3/bin:\$PATH\"" >> ~/.bashrc
export PATH="$HOME/anaconda3/bin:$PATH"
conda install -y bcolz
conda upgrade -y --all
source ~/.bashrc

# setup Anaconda enviornment
echo "Setting up Anaconda enviornment for Algorithmica"
wget https://raw.githubusercontent.com/thegreatskywalker/my_deep_learning/master/Anaconda_Setup/linux_tensorflow_gpu.yml
conda env create -f linux_tensorflow_gpu.yml

# configure jupyter and prompt for password
jupyter notebook --generate-config
jupass=`python -c "from notebook.auth import passwd; print(passwd())"`
echo "c.NotebookApp.password = u'"$jupass"'" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False" >> $HOME/.jupyter/jupyter_notebook_config.py

# clone the Algoritmica course repo and prompt to start notebook
cd ~
git clone https://github.com/algorithmica-repository/deep-learning
echo "\"jupyter notebook\" will start Jupyter on port 8888"
echo "If you get an error instead, try restarting your session so your $PATH is updated"