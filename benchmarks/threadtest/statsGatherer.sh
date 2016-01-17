#!/usr/bin/env bash

export LD_PRELOAD=$2
logname=$1
rm $1
for i in {1..30}; do
  ./threadtest >> $1
done
