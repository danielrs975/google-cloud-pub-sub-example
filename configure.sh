#!/bin/sh

echo "Configuring the environment..."

rm -r env/
mkdir env/
virtualenv env/ --python=python3
pip install --upgrade google-cloud-pubsub

echo "We are ready!!"