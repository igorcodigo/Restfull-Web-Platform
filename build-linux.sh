#!/bin/bash

set -e
set -x

function BuildRestfulWebPlatformContainer () {
  APP_VERSION=$(grep "LABEL APP_VERSION" docker/Dockerfile | grep -o '"[^"]*"' | sed 's/"//g')
  docker build . -t restful-web-platform:"${APP_VERSION}" -f docker/Dockerfile --no-cache
}

BuildRestfulWebPlatformContainer
