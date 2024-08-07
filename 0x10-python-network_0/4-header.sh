#!/bin/bash
# A script takes in a URL, sends a GET request with a header
curl -s -H "X-School-User-Id: 98" "$1"
