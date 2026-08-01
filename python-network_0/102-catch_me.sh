#!/bin/bash
# Follows redirects and cookies on the catch_me route until the final response
curl -s -L -c /tmp/catch_me_cookies -b /tmp/catch_me_cookies "0.0.0.0:5000/catch_me"
