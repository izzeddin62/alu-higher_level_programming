#!/bin/bash
# return You got me! in rhe response body
curl -sL -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me"
