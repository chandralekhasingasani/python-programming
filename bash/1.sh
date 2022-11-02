#!/bin/bash
valid=true
count=1
while [ $valid ];
do
  echo ${count}
  count=$((count + 1))
  if [ ${count} -eq 6 ];
  then
    valid=false
    break
  fi
done
