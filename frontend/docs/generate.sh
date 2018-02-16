#!/usr/bin/env bash
set -e

if [[ "$(docker images -q binaryedge/docs 2> /dev/null)" == "" ]]; then
    docker build -t binaryedge/docs .
fi

docker run -v $(pwd):/app binaryedge/docs aglio -i blueprint.apib -o api.html

open api.html