#!/bin/sh

set -e

# Install ssh private key
if [ -z "SSH_KEY" ]; then
    exit 1
else
    mkdir -p /root/.ssh
    echo "$SSH_KEY" > /root/.ssh/id_rsa
    chmod 600 /root/.ssh/id_rsa
fi

# Store Ansible control path in memory file system, since docker overlayfs
# can break the socket
export ANSIBLE_SSH_CONTROL_PATH="/dev/shm/ansible-ssh-%%h-%%p-%%r"
