#!/bin/bash

./list_contract.sh | sed 's/[0-9]//g' | sort | uniq
