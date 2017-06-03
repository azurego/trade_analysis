#!/bin/bash

cut -f3 -d, trade_sample.csv | grep -v contract | sort | uniq
