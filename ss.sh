#!/bin/bash

line=1
while true;do
now=$(date +"%T")
echo $line
echo "$line Current time : $now" >> /tmp/log
let line=line+1
sleep 1
done
