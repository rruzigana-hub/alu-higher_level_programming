#!/bin/bash
# Follows redirects on the catch_me route until the final response
curl -s -L "0.0.0.0:5000/catch_me"
