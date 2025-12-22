#!/usr/bin/env bash
set -e

rm -rf build opentofu/lambda.zip

docker run --rm \
  --entrypoint /bin/bash \
  -v "$PWD":/var/task \
  -w /var/task \
  public.ecr.aws/lambda/python:3.11 \
  -lc '
    set -e

    # Instalar zip si no está
    if ! command -v zip >/dev/null 2>&1; then
      yum -y update
      yum -y install zip
    fi

    python -m pip install --upgrade pip
    pip install -r requirements.txt -t build
    cp -r app build/app
    cd build
    zip -r9 /var/task/opentofu/lambda.zip .
  '