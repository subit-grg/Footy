#!/bin/bash
declare -a directories=("front-end" "stadium-s2" "condition-s3" "opps-s4")
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
source venv/bin/activate
pip3 install -r test_requirements.txt
python3 -m venv venv
for dir in "${directories[@]}"
do
  cd ${dir}
  pwd
  python3 -m pytest --cov=application 
  pwd
  cd ..
done