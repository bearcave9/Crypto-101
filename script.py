#!/usr/bin/python

import sys
import csv

N = raw_input("Please enter N: ")
with open(sys.argv[1], 'r') as raw:
            
    for i in range(int(N)+1):
        line  = raw.next().strip()
        print line
    
raw.close()            








