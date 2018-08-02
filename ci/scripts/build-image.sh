#!/bin/sh

set -e

. `dirname $0`/global.sh

# Extract artifact
# cd release
# tar xzf source.tar.gz --strip 1
cd master
# Run packer
cd packer

export PACKER_LOG=1

packer build ./$CI_COMPONENT.json
