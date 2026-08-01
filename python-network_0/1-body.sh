#!/bin/bash
# Sends a GET request and displays the body only if the final status code is 200
BODY=$(mktemp); CODE=$(curl -s -L -o "$BODY" -w "%{http_code}" "$1"); [ "$CODE" = 200 ] && cat "$BODY"; rm -f "$BODY"
