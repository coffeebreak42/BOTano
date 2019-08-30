#!/bin/bash

# Save current directory in OLD_DIR
OLD_DIR=$PWD
# Change directory to where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

docker build -t coffeebreak/spotify_crawler .
xargs -d '\n' -a $1 docker run -it --name coffeebreak_spotify_crawler coffeebreak/spotify_crawler
rc=$?
docker cp coffeebreak_spotify_crawler:/app/output.json .
docker rm coffeebreak_spotify_crawler

# Go back to the former current directory
cd $OLD_DIR

echo "Exiting from container with status $rc"
exit $rc
