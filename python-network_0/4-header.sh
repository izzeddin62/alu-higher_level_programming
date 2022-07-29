#!/bin/bash
# sends a GET request to the URL,X-School-User-Id header and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
