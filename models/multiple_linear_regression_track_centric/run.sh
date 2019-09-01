#!/bin/bash

# Save current directory in OLD_DIR
OLD_DIR=$PWD
# Change directory to where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

cp $1 input
docker build -t coffeebreak/multiple_linear_regression_track_centric --build-arg data=input .
rm input
docker run -it --name coffebreak_multiple_linear_regression coffeebreak/multiple_linear_regression_track_centric
docker cp coffebreak_multiple_linear_regression:/app/images .
docker rm coffebreak_multiple_linear_regression
rc=$?

# Go back to the former current directory
cd $OLD_DIR

echo "Exiting from container with status $rc"
exit $rc
