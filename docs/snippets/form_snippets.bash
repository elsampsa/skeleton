#!/bin/bash

# # choose your python flavor
exe="python"
# exe="python3"

# # list here your example snippets
codes="example1.py example2.py" 

for i in $codes
do
    echo $i
    $exe pyeval.py -f $i > $i"_"
done
