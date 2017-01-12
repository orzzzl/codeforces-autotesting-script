#!/bin/bash
set -e

a=$(echo $1 | tr 'a-z' 'A-Z')
echo $a

for f in $a*.in
do
    echo "testing ${f:0:2}..."
    echo "sample input:"
    cat $f
    echo "#################################"
    echo "your output:"
    g++ -std=c++11 -Wl,-stack_size,0x100000000 $a.cpp && a.out < $f
    echo ""
    echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    echo "correct output:"
    cat ${f:0:2}.out
    echo ""
    echo ""
    echo ""
done
