#!/bin/bash
directory='./'
find $directory -type f -exec du -h {} + | sort -rh | head -n 1