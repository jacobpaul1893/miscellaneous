#!/bin/bash 

for i in $(last -R | awk '{print $1}' | grep -v "reboot" | grep -v "wtmp" | sort | uniq)
do
    last -R | grep -i "$(date | awk '{print $2, $3}')" | sed -n "/$i/p" | tail -1 | awk '{print $1, $6}' >> first_login.txt
    last -R | grep -i "$(date | awk '{print $2, $3}')" | sed -n "/$i/p" | head -1 | awk '{if ($8 == "logged") print $1, "online"; else print $1, $8}' >> last_logout.txt
done


last -R | grep -i "$(date | awk '{print $2, $3}')" | grep -v reboot | awk '{print $1, $6, $9}' >> dn.txt


python3 login_final.py

rm -f *.txt
