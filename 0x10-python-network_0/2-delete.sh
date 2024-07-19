#!/bin/bash
# A script takes in a URL, sends a DELTET request and display the body
curl -sX DELETE "$1"
