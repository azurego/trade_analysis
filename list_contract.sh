#!/bin/bash

grep -v "^#" trade_sample.csv | cut -f3 -d, | sort | uniq
