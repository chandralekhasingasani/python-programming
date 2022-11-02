#!/bin/bash


arr=()
for (( counter=0;counter<2;counter++))
do
    threadId=$(read line; echo ${line} |  cut -d " " -f3)
    echo $threadId
    arr+=(${threadId})
done

min=${arr[0]}
for i in "${arr[@]}"
do
    if [[ $min -ge $i ]];
    then
      min=$i
    fi
done

echo ${min}

${}