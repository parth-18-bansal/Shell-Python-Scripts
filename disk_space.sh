#!/bin/bash
threshold=2
current_usage=$(df / | grep / | awk '{print $5}' | sed 's/%//g')
if [ "$current_usage" -gt "$threshold" ]
then
    echo "Disk space is running out. Current usage is $current_usage%"
else
    echo "Disk space is normal. Current usage is $current_usage%"
fi