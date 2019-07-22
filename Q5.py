"""Write a program to print the Fibonacci series up to the number 34. 
(Example: 0, 1, 1, 2, 3, 5, 8, 13, … The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)"""

fib1 = 0
fib2 = 1
c = 0
print(fib1)
print(fib2)
for i in range(2,34):
    c=fib1+fib2
    fib1=fib2fib2=c
print(c,end=" ")   