# dynamic-programming-practice-python
Practising dynamic programming in Python


## Chapter 1: Fibonacci

    Fibonacci sequence can be expressed as:
     The Rule is: 
       x8 = x7 + x6
     which can also be expressed as:
       xn = xn−1 + xn−2

Using recursion it's possible to calculate the fibonacci value for n. However as n gets higher so does the calculation time. Recursion is an option but inefficient.

Dynamic progamming is much more efficient because it will cache the fibonacci value of each number up to n which will prevent recalculation of fibonacci numbers that have been solved already.

The efficiency comparison is drastic. 

Solving for fibonacci 35 using: 

   - recursion takes Total: 0:00:14.072584
   - dynamic programming Total: 0:00:00.000057

