miniconda3
python 3.11
cuda 121 or 118

##for fedora

sudo dnf groupinstall 'Development Tools'
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-fedora37-12-1-local-12.1.0_530.30.02-1.x86_64.rpm
sudo rpm -i cuda-repo-fedora37-12-1-local-12.1.0_530.30.02-1.x86_64.rpm
sudo dnf clean all
sudo dnf -y module install nvidia-driver:latest-dkms
sudo dnf -y install cuda-12-1

echo "export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}" >> ~/.profile
source ~/.profile

##for fedora

conda create -n bo245 python=3.11.5 pip setuptools
conda activate bo245

git clone https://github.com/MuhammadMoinFaisal/YOLOv8-DeepSORT-Object-Tracking.git
cd YOLOv8-DeepSORT-Object-Tracking/
pip install -e '.[dev]'
pip install torch hydra-core opencv-python easydict
conda install pycuda
pip install paho-mqtt python-etcd
pip install ultralytics==8.0.0
pip install openvino-dev[tensorflow2,onnx]

rename to YOLOv8_deepsort_count

pip3 install gdown
cd ./YOLOv8-DeepSORT-Object-Tracking/ultralytics/yolo/v8/detect
gdown "https://drive.google.com/uc?id=11ZSZcG-bcbueXZC3rN08CM0qqX3eiHxf&confirm=t"

pip3 install adafruit-io
