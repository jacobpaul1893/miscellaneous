#!/bin/bash

x=$(./ld.sh | awk '{print $1}' | uniq)

for i in $x
do
  ac -p -d $i | tail -1 | sed "s/total/$i/g"
done
