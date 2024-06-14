#!/usr/bin/env bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg texlive-full
pip3 install manim
pip3 install -r requirements.txt
