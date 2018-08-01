#!/bin/sh

set -e

source `dirname $0`/global.sh

cd master/tests/$CI_COMPONENT

kitchen test --destroy=always
