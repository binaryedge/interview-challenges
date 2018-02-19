#!/usr/bin/env bash

if [ "$1" != 'build' ] && [ "$1" != 'show_emails' ] && [ "$1" != 'server' ] && [ "$1" != 'create_user' ]; then
  echo "->1st Argument Env: build, show_emails, server or create_user"
  echo "e.g.: ./setup.sh build"
  exit 1
fi

if [ -n "$1" ] && [ $1 = "build" ]; then

    echo "---------------------"
    echo "Build docker image..."
    echo "---------------------"

    cd api

    docker build -t binaryedge/be-dataleaks-example-api .
fi

if [ -n "$1" ] && [ $1 = "show_emails" ]; then

    echo "---------------------"
    echo "Show all emails..."
    echo "---------------------"

    cd api

    docker run --rm  \
      -v $(pwd):/code/ \
      binaryedge/be-dataleaks-example-api python3 manage.py show_emails

fi

if [ -n "$1" ] && [ $1 = "server" ]; then

    echo "---------------------"
    echo "Run Server on Port 8000..."
    echo "---------------------"

    cd api

    docker run --rm  \
      --name be-dataleaks-example-api \
      -p 8000:8000 \
      -v $(pwd):/code/ \
      binaryedge/be-dataleaks-example-api

fi

if [ -n "$1" ] && [ $1 = "create_user" ]; then

    echo "---------------------"
    echo "Create an user..."
    echo "---------------------"

    cd api

    docker run --rm -i -t -v $(pwd):/code/ binaryedge/be-dataleaks-example-api python3 manage.py createsuperuser

fi
