Calclute Time Complexity for the Tasks Below:

"""
TASK 0:
->What is the first record of texts and what is the last record of calls? 
  The Task 0 running time is independent of the input size n as we are looking for a specific value, so the notation is O(1)
"""

"""
TASK 1:
->How many different telephone numbers are there in the records? 
  The Task 1 running time is dependent of the input size n as the code has a for loop which iterates all items in the list and adds into
  a set, so the notation is O(n).
"""

"""
TASK 2:
->Which telephone number spent the longest time on the phone during the period? Don't forget that time spent answering a call is also time spent on the phone.
  The Task 2 running time is same as Task 1 and we are inserting into a Dictionary object which has the unique values, so the notation is O(n).
"""

"""
TASK 3:
->Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.
   The Task 3 Part A running time is logarthmic because there are dependency conditions and the statements associated to it and the sorting function 
   builds a new list to compute in lexicographic order.The notation is O(nlogn).
->Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore?
   The Task 3 Part B running time completes in linear time as it checks the conditions and increments through the counts to get a percentage. The notation is O(n)
"""

"""
TASK 4:
->The telephone company want to identify numbers that might be doing telephone marketing.
   The Task 4 has a loop operation to add into individual sets and perform a difference operation. The sorting function 
   builds a new list to compute in lexicographic order. The running time is logarthmic. The notation is O(nlogn).
"""
