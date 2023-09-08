#!/bin/bash

array=($(cat /etc/wpa_supplicant/wpa_supplicant.conf | egrep 'psk' | awk -F'"' '{print $2}'))

i=0
for variable in $( cat /etc/wpa_supplicant/wpa_supplicant.conf | egrep 'ssid="' | awk -F'"' '{print $2}')
do
        echo [+] $variable : ${array[$i]}
        ((i=i+1))
done
