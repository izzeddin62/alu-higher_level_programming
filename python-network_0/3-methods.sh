#!/bin/bash
# print the length of the response
curl -sI $1 | head -7 | tail -1 | cut -c 8-
