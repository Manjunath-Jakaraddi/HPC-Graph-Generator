#!/bin/bash

##################################################|
#-------------------------------------------------|
#Data Section                                     |
#-------------------------------------------------|
# 1] Number of Threads 
declare -a threads=(1 2 4 8)

# 2] Input Size Initial, Final and Incremental Value
value_start=250
value_incr=250
value_end=1000
#-------------------------------------------------|
##################################################|


#Running the mentioned program in loop and saving the readings to csv file
gcc $1 -fopenmp
rm -f out.csv
for thread in "${threads[@]}" 
do
	value=$value_start
	while [ $value -le $value_end ]
	do
		./a.out $value $thread >> out.csv
		((value+=value_incr))
	done
	echo >> out.csv
done

#generating the graph using the csv file
python3 graph_generator.py
