print("Hello, World!")
print("Hello, Muttal")
print("g&du2")
def fibonacci(n):
    # Initialize the first two numbers in the Fibonacci series
    fib_series = [0, 1]
    
    # Generate Fibonacci series up to the nth number
    for i in range(2, n):
        next_fib = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_fib)
    
    return fib_series

# Example: Get the first 10 numbers in the Fibonacci series
n = 10
fib_sequence = fibonacci(n)

# Print the Fibonacci series
print(f"The first {n} numbers in the Fibonacci series are:")
print(fib_sequence)

