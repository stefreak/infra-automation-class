#!/bin/sh

set -e

source `dirname $0`/global.sh

cd master/tests/loadbalancer

kitchen test --destroy=always
