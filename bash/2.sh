#!/bin/bash
count=1
echo "Counter="
read count
for (( counter=${count};counter>0; counter--))
do
  echo $counter
done

counter=39
if [ ${counter} -lt 10 ];
then
  echo "Single digit"
else
  echo "double digit"
fi