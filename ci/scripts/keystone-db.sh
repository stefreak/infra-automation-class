#!/bin/sh

set -e

source `dirname $0`/global.sh

cd master/tests/keystone-db

kitchen test --destroy=always

