#!/bin/sh

echo "Configuring the environment..."
export GOOGLE_APPLICATION_CREDENTIALS="./key.json"
echo $GOOGLE_APPLICATION_CREDENTIALS
echo "We are ready!!"