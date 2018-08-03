#!/bin/sh

set -e

. `dirname $0`/global.sh

# Extract artifact
cd release
tar xzf source.tar.gz --strip 1

# Run packer
cd packer

packer build ./$CI_COMPONENT.json
