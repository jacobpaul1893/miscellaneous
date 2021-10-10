#!/bin/bash

keyboard_id=$(xinput -list | grep -i "AT Translated Set 2 keyboard" | cut -d "=" -f2 | awk '{print $1}')
xinput float $keyboard_id
