"""Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23 + 1/33 + 1/43 + …… + 1/n3"""

n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum+=1/i**3
print(f"sum of series={sum}")