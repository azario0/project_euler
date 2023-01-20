'''This problem 1 from Project Euler '''
'''This is my solution .'''
#This is a comment !
#To plot the time consumed while making calculations with the two functions
import matplotlib.pyplot as plt
import numpy as np 

#To test the efficiency of the algorithmes .
import time

#I've done that to prevent the program from crashing .
import sys

#To plot the time difference between the two solutions .
import matplotlib.pyplot as plt

#I've put the limit above our neef in the recursion so the program won't crash .
sys.setrecursionlimit(1500)

#The recursive solution
def mul_3_rec(tab,rg):
    if rg<0:
        return tab
    else :
        if rg%3==0 or rg%5==0:
            tab.append(int(rg))
        rg=rg-1
        tab=mul_3_rec(tab,rg)
    return tab

#The normal function solution .
def mul_3(rg):
    multiples_of_3=[]
    for i in range(rg):
        if i%3==0 or i%5==0:
            multiples_of_3.append(i)
    return sum(multiples_of_3)



#Testing the normal function
t1_start = time.time()
sm=mul_3(1000)
t1_stop = time.time()
print("Here's the sum of the normal function : : ",sm)
print("Here's the time it took to make the calculations :",t1_stop-t1_start)

#testing the recursive function
t2_start = time.time()
tab=[]
sm=sum(mul_3_rec(tab,999))

t2_stop = time.time()
print("Here's the sum of the recursive function : ",sm)
print("Here's the time it took to make the calculations :",t2_stop-t2_start)



function1_time=[]
function2_time=[]
for i in range(10):
    t1_start = time.perf_counter ()
    sm=mul_3(1000)
    t1_stop = time.perf_counter ()
    function1_time.append(t1_stop-t1_start)
    t2_start = time.perf_counter ()
    tab=[]
    sm=sum(mul_3_rec(tab,999))
    t2_stop = time.perf_counter ()
    function2_time.append(t2_stop-t2_start)

fig, ax = plt.subplots()
index = np.arange(10)
bar_width = 0.4
opacity = 0.7
print(function1_time,function2_time)
rects1 = plt.bar(index, 
function1_time,
bar_width,
color='black',
label='function 1')

rects2 = plt.bar( index+ bar_width,
function2_time,
bar_width,
color='blue',
label='function 2 (recursive)')
plt.xlabel('calls')
plt.ylabel('Time consumed')
plt.title('Scores by person')
plt.legend()
plt.tight_layout()
plt.show()