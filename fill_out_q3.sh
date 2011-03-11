#!/bin/bash

ns=( 1 5 10 20 50 100 150 200 250 )
 
for n in "${ns[@]}" 
do
	echo "Test accuracy: N=$n"
	test_acc_array=`./TBL_classify.sh  examples/test2.txt model_file sys_output $n`
	echo "${test_acc_array[0]}"
	echo -e "\n"
done
