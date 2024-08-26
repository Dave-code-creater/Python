#!/bin/bash

if ! command -v choco &> /dev/null
then
    echo "Chocolatey is not installed."
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    exit
fi


# Install Python
choco install python3 -y

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Install PyTorch
pip install torch torchvision torchaudio

# Install the Whisper model
pip install openai-whisper

