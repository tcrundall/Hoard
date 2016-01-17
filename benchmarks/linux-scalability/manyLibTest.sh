#!/usr/bin/env bash

./singleLibTest.sh glib.log 
./singleLibTest.sh hoard.log ~/src/Hoard/src/libhoard.so
./singleLibTest.sh tcmalloc.log ~/src/gperftools/build/.libs/libtcmalloc.so
