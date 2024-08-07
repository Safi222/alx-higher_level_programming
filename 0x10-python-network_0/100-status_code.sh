#!/bin/bash
# A script takes in a URL, sends a request and display the status code
curl -s -o /dev/null -w "%{response_code}" "$1"
