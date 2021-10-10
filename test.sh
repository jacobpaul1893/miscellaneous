#!/bin/bash

last -R | grep -i "$(date | awk '{print $2, $3}')" | awk '/^[^reboot]/ {print $1, $6, $9}' > tst.txt
