#!/bin/bash

pid=`cat server.pid`
#if [ ! -e /proc/$pid -a /proc/$pid/exe ]; then
kill $pid
rm server.pid
#fi