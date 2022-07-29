#!/bin/bash
# return You got me! in rhe response body
curl -sL -H -d "user_id=98" -X PUT "0.0.0.0:5000/catch_me"
