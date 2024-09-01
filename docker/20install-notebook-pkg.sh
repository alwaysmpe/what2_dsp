#!/bin/bash

echo "start"
OUTPUT=`pip list | grep -q notebooks | echo`
echo "output of pip:"
echo "${OUTPUT}"

if [ -z "$OUTPUT" ]; then
    pip install -e /notebooks/
fi
