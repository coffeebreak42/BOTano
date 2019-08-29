#!/bin/bash

# Save current directory in OLD_DIR
OLD_DIR=$PWD
# Change directory to where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

docker build -t coffeebreak/spotify_crawler .
xargs -d '\n' -a $1 docker run --rm -it coffeebreak/spotify_crawler
rc=$?

# Go back to the former current directory
cd $OLD_DIR

echo "Exiting from container with status $rc"
exit $rc
