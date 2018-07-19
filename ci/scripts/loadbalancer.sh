#!/bin/sh

set -e

exec `dirname $0`/global.sh

cd master/tests/loadbalancer

kitchen converge
