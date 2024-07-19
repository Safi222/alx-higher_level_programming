#!/bin/bash
# A script causes the server to respond with a message containing You got me!
curl -sL -X PUT -H "Origin: School" -d "user_id=98" --http1.0 0.0.0.0:5000/catch_me
