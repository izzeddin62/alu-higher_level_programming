#!/bin/bash
# print the length of the response
curl -s $1 | wc -m
