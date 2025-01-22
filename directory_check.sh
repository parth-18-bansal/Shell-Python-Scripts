#!/bin/bash
DIRECTORY="/shellScriping"
if [[ ! -d $DIRECTORY ]]; then
    echo "Directory does not exist"
    mkdir -p $DIRECTORY
else
    echo "Directory exists"
fi