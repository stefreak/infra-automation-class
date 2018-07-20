#!/bin/sh

set -e

source `dirname $0`/global.sh

cd master/tests/loadbalancer

# Fix ansible control path
export ANSIBLE_SSH_CONTROL_PATH=/dev/shm/ansible-ssh-%%h-%%p-%%r

kitchen test
