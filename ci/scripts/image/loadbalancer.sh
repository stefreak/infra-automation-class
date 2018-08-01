#!/bin/sh

set -e

source `dirname $0`/../global.sh

# Extract artifact
cd release
tar xzf source.tar.gz

ls -laR

cd source/packer
packer build ./loadbalancer.json
