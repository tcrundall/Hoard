#!/usr/bin/env bash

./statsGatherer.sh glib.log
./statsGatherer.sh tcmalloc.log ~/src/gperftools/build/.libs/libtcmalloc.so
./statsGatherer.sh hoard.log ~/src/Hoard/src/libhoard.so

echo glib
./extractor.py -f glib.log
echo tcmalloc
./extractor.py -f tcmalloc.log
echo hoard
./extractor.py -f hoard.log
