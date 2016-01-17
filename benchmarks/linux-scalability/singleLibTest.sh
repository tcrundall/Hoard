#!/usr/bin/env bash

export LD_PRELOAD=$2
logname=$1

rm $1
echo here
for i in {1,2,4,8}; do
  echo $i
  ./linux-scalability 512 1000000 $i >> $1
done
