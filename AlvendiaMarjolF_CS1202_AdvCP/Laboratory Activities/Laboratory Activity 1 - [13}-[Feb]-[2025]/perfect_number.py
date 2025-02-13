num = int(input("Enter a number: "))
j = 0
for i in range(1,num):
    if num % i == 0:
        j += 1
if num == j:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

    
    