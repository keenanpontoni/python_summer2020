import matplotlib.pyplot as plt
import math
import numpy as np
import array
import random
import datetime

##first, I creat a few lists for purpose of testing:

test_a = [5, 9, 4]
test_b = [3, 4, 2, 1, 9, 7]
test_c = [12, 1, 0, 5, 4, 6, 15, 19]

##for reference, we should yield the following orders:
##test_a = [4, 5, 9]
##test_b = [1, 2, 3, 4, 7, 9]
##test_c = [0, 1, 4, 5, 6, 12, 15, 19]




##let's first try selection_sort

def insertion_sort(numbers):
    numbers = numbers.copy()
    for i in range(0, len(numbers)):
        k = i-1
        plus_one = numbers[i]           
        
        while (numbers[k] > plus_one) and (k >=0):
            numbers[k+1] = numbers[k]
            k=k-1
        numbers[k+1] = plus_one
        
    return numbers



##To test the the sorting method:

selection_sort(test_a)

##[4, 5, 9]

selection_sort(test_b)

##[1, 2, 3, 4, 7, 9]

selection_sort(test_c)

##[0, 1, 4, 5, 6, 12, 15, 19]

##Unsurprisingly, the lists all sorted correctly.



##For the second one, try Bubble Sort:
##Note: I couldn't quite get this code to work and relied on code I found online.

def bubble_sort(numbers):
    for i in range(0, len(numbers)):
        for k in range(i):
            if numbers[k]>numbers[k+1]:
                next = numbers[k]
                numbers[k] = numbers[k+1]
                numbers[k+1] = next

    return numbers 



##first generate a random sample:
def simulate(number):
    simulation = []
    for i in range(0, 100):
        randsamp = random.sample(range(0, number), 100)
        simulation.append(randsamp)
    return simulation


# Now that I have my simulation data, I need to father the runtime data in a function


def time_test(number, algorithm):
    sim_list = simulate(number)
    algorithm_list = algorithm
    algorithm_time =[]

    for i in range(0, number):
        start = datetime.datetime.now()
        end = datetime.datetime.now() - start
        algorithm(sim_list[i])
        algorithm_time.append(end.microseconds)

    return algorithm_time


##used help from Jenna for plotting part.


x = list(range(1,100))
insertion_mean = []
bubble_mean = []

for i in x:
   insertion_means = np.mean(time_test(i, insertion_sort)[0])
   insertion_mean.append(insertion_means)


for i in x:
   bubble_means = np.mean(time_test(i, bubble_sort)[1]) 
   bubble_mean.append(bubble_means)

  
plt.plot(x, insertion_mean, 'g-', label = "Insertion Sort")
plt.xlabel('Sample Size')
plt.ylabel('Mean Sorting Time')
plt.legend()
plt.show()


plt.plot(x, bubble_mean, 'g-', label = "Bubble Sort")
plt.xlabel('Sample Size')
plt.ylabel('Mean Sorting Time')
plt.legend()
plt.show()


##ahhhh, getting an error re: sample size dimensions.




