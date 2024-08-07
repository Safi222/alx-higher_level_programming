#!/bin/bash
# A script takes in a URL and file, and sends a json POST request
curl -s -d "`cat $2`" -H "Content-Type: application/json" "$1"
