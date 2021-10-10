#!/bin/bash

for i in $(ls /home);
do
  last -R $i | grep -i "$(date | awk '{print $2, $3}')"
done
