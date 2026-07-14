def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci Numbers:")

for num in fibonacci(10):
    print(num, end=" ")

print()
print("\nFirst 4 Fibonacci Numbers using next():")

fib = fibonacci(10)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))