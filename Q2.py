"""Write a program to accept a number “n” from the user; then display the sum of the following series:
1 + 1/2 + 1/3 + ……. + 1/n"""

n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
    sum+=1/i
print(f"sum of series={sum}")