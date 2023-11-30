#!/bin/bash
#curl request respond size view
curl -so /dev/null -w '%{size_download}\n' "$1"
