#!/bin/bash

# Save current directory in OLD_DIR
OLD_DIR=$PWD
# Change directory to where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

cp $1 input
docker build -t coffeebreak/model-tensorflow --build-arg data=input .
rm input
docker run -it --rm coffeebreak/model-tensorflow
rc=$?

# Go back to the former current directory
cd $OLD_DIR

echo "Exiting from container with status $rc"
exit $rc
