#!/bin/bash
# A script takes in a URL, and display all HTTP methods available
curl -sIX OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-
