#!/bin/bash -x

SCRIPT_DIR="$(dirname $0)"
IMAGE=${1:-cortx-status}
BUILD_URL=http://cortx-storage.colo.seagate.com/releases/cortx/github/main/centos-7.9.2009/last_successful_prod
mkdir tmp/
cp -f  ../dist/*.noarch* tmp/
STATUS_RPM=$(ls tmp/ | grep noarch)
docker build --build-arg RPM="$STATUS_RPM" --build-arg BUILD_URL=$BUILD_URL -t $IMAGE $SCRIPT_DIR
rm -rf tmp/
