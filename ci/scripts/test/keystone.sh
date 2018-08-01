#!/bin/sh

set -e

source `dirname $0`/../global.sh

cd master/tests/keystone

kitchen test --destroy=always
