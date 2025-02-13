fib = int(input("Enter number of terms: "))
first = 0
second = 1
print("Fibonacci Series:", end=" ")
for i in range(fib):
        print(first, end=" ")
        first, second = second, first + second
       