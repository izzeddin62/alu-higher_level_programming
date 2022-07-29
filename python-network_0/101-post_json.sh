#!/bin/bash
# print the status code
curl -sH "Content-Type: application/json" --data "$(cat $2)" -X POST $1
