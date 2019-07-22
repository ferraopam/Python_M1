	#Write a program to accept a number and determine whether it is a prime number or not.

n=int(input("Enter the value of n:")
if n<2:
   print(f"{n} is not prime")
   else:
       for i in range(2,n/2):
        if n%i==0:
           print(f"{n} is a prime number")
        else:
            print(f"{n} is not prime number")
