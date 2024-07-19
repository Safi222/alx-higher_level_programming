#!/bin/bash
# A script takes in a URL, sends a POST request with a header
curl -s --data "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
