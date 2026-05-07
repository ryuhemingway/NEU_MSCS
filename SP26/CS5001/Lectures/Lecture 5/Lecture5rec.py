call_count = 0

def fibonacci_counted(n):
    global call_count
    call_count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_counted(n - 1) + fibonacci_counted(n - 2)

call_count = 500
result = fibonacci_counted(10)
print(f"fibonacci(10) = {result}")
print(f"Number of function calls: {call_count}")
# Output: 177 calls!