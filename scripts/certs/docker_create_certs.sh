#!/bin/sh
# Creates a couple of locally valid SSL certificates using a Docker Container

DOCKER=$(which docker)
[ ! -x "${DOCKER}" ] && \
  echo "You don't seem to have Docker installed" && \
  exit 1

$DOCKER build -t cert-builder .
$DOCKER run -v $(pwd):/app -t cert-builder bash /app/create_certs.sh

echo "Done! Check the 'ssl' folder"
