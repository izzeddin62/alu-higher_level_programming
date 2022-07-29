#!/bin/bash
# send a post request with 2 variable and print the response
curl -sb -X POST --data "email=test@gmail.com&subject=I will always be here for PLD"  $1
