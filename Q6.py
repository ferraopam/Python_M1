#Write a program to accept a number from the user; then display the reverse of the entered number.


num=int(input("enter a number"))
rev = 0
while (num > 0):
    rem=num % 10
    rev = (rev * 10) + rem 
    num=num // 10
print(f"reverse of entered number",rev)

