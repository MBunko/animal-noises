#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

# Test service 1
cd service_1
python3 -m venv venv
pip3 install -r requirements.txt
pip3 install pytest pytest-cov
pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

# Test service 2
cd service_2
python3 -m venv venv
pip3 install -r requirements.txt
pip3 install pytest pytest-cov
pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
