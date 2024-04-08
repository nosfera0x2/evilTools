#!/bin/bash

 for i in {1..31}; do ping -c 1 10.0.141.$i | fgrep ttl & done 2>/dev/null | sed -e 's/^.*from //' -e 's/:.*$//' | sort -n -t. -k4
