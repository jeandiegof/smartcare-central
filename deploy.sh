#!/bin/zsh
set -e

# This is not secure and should be used only for development purposes
TARGET_PASSWORD="raspberry"
TARGET_USER="pi"
TARGET_HOSTNAME="smartcare.local"

SSHPASS=$TARGET_PASSWORD sshpass -e scp src/*.py $TARGET_USER@$TARGET_HOSTNAME:/home/pi/smartcare-central/src
