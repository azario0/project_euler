#To see how much time it would require the function to run
import time


#To plot the time consumed while making calculations with the two functions
import matplotlib.pyplot as plt
import numpy as np 


def fib_even_valued_terms_sum(rg):
    previous , current,summ=0,1,0
    for i in range(rg):
        if current>rg:
            return summ
        elif current%2==0 :
            summ+=current
        previous,current=current,previous+current

def fib_even_valued_terms_sum_rec(rg,previous=0,current=1,summ=0):
    if current>rg:
        return summ
    elif current%2==0:
        summ+=current
    previous,current=current,previous+current  
    return fib_even_valued_terms_sum_rec(rg-1,previous,current,summ)

def fib_even_valued_terms_sum_inf(rg):
    previous,current,summ=0,1,0
    while True:
        if current>rg:
            return summ
        elif current%2==0:
            summ+=current
        previous,current=current,previous+current


val=4000000
t1_start = time.perf_counter ()
print("The result of a normal function with a for loop",fib_even_valued_terms_sum_rec(val))
t1_stop = time.perf_counter ()

t2_start = time.perf_counter ()
print("The result of a recursive function",fib_even_valued_terms_sum_rec(val))
t2_stop = time.perf_counter ()

t3_start = time.perf_counter ()
print("The result of a normal function with a while loop",fib_even_valued_terms_sum_inf(val))
t3_stop = time.perf_counter ()

print("The consumed time of the normal function with a for loop is: ",t1_stop-t1_start)
print("The consumed time of the recursive function is: ",t2_stop-t2_start)
print("The consumed time of the normal function with an infinite while loop is: ",t3_stop-t3_start)

fun1,fun2,fun3=[],[],[]
for i in range(10):
    t1_start = time.perf_counter ()
    res=fib_even_valued_terms_sum_rec(val)
    t1_stop = time.perf_counter ()
    fun1.append(t1_stop-t1_start)

    t2_start = time.perf_counter ()
    res=fib_even_valued_terms_sum_rec(val)
    t2_stop = time.perf_counter ()
    fun2.append(t2_stop-t2_start)

    t3_start = time.perf_counter ()
    res=fib_even_valued_terms_sum_inf(val)
    t3_stop = time.perf_counter ()
    fun3.append(t3_stop-t3_start)


ax = plt.subplot()
index = np.arange(10)

ax.bar(index-0.2, fun1, width=0.2, color='b', align='center',label='For loop function')
ax.bar(index, fun2, width=0.2, color='g', align='center',label='Recursive function')
ax.bar(index+0.2, fun3, width=0.2, color='r', align='center',label='Infinite loop function')

plt.xlabel('calls')
plt.ylabel('Time consumed')
plt.legend()
plt.tight_layout()
plt.show()