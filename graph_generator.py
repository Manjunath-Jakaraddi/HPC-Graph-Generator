from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv

##################################################|
#-------------------------------------------------|
#Data Section                                     |
#-------------------------------------------------|
# 1] Number of Threads                            
threads=[1,2,4,8]

# 2] Input Size Initial, Final and Incremental Value
value_start=250
value_incr=250
value_end=1000
#-------------------------------------------------|
##################################################|


#Data for the Graphs extracting from the csv file
file_name = "out.csv"
exec_times = []
input_sizes = []
with open(file_name,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        inp = []
        row = row[:-1]
        for i in row:
            inp.append(float(i))
        exec_times.append(inp)
exec_times=np.array(exec_times)
for i in range(value_start,value_end+value_incr,value_incr):
    input_sizes.append(i)


#Setting of Styles and subplot orientations
plt.style.use('seaborn-white')
f,ax = plt.subplots(2,1)

# Drawing of Input Size v/s Execution Time Graph
ax[0].set_title('Input Size v/s Execution Time')
ax[0].set_xlabel('Input Size')
ax[0].set_ylabel('Execution Time(in seconds)')
for cnt,thrd in enumerate(threads):
    ax[0].plot(input_sizes,exec_times[cnt],label="Threads "+str(thrd))
ax[0].legend()

#Drawing of Number of Threads v/s Execution Time Graph
ax[1].set_title('Number of Threads v/s Execution Time')
ax[1].set_xlabel('Number of Threads')
ax[1].set_ylabel('Execution Time(in seconds)')
for cnt,size in enumerate(input_sizes):
    ax[1].plot(threads,exec_times[:,cnt],label="Input Size "+str(size))
ax[1].legend()
plt.show()
