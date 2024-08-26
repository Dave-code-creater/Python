#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required packages
pip3 install -r requirements.txt

# Install pytorch
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install the whipser model
pip install -U openai-whisper