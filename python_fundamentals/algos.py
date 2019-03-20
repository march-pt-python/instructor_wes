# Create a function to generate Fibonacci numbers. In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1. Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc). Examples: fibonacci(0) = 0 (given), fibonacci(1) = 1 (given), fibonacci(2) = 1 ( fib(0) + fib(1) , or 0+1), fibonacci(3) = 2 ( fib(1) + fib(2) , or 1+1), fibonacci(4) = 3 (1+2), fibonacci(5) = 5 (2+3), fibonacci(6) = 8 (3+5), fibonacci(7) = 13 (5+8), etc.

    # start with 0 and 1
        # what does it mean to start with 0 and 1?
        # store 0 and 1 in a list
        # store 0 and 1 in separate variables
    # to get to the next number, add previous 2 numbers together
        # how can I know which numbers are the 2 previous numbers?
        # what does it mean to "get to" the next number?
            # current = a + b
            # a = b
            # b = current
    # stop when I have idx + 1 total values
        # how do I stop?
        # how do I start?
def fibonacci(idx):
    if idx <= 1:
        return idx

    a = 0
    b = 1
    for i in range(idx - 1):
        current = a + b
        a = b
        b = current
    return current

# print(fibonacci(100))
# print(fibonacci(1))
# print(fibonacci(0))

def fibonacci_with_list(idx):
    results = [0, 1]
    if idx <= 1:
        return results[idx]

    for i in range(2, idx + 1):
        results.append(results[i - 1] + results[i - 2])
    return results[len(results) - 1]

# print(fibonacci_with_list(7))
# print(fibonacci_with_list(1))
# print(fibonacci_with_list(0))

def rfib(index):
    if(index == 0):
        return 0
    elif(index == 1):
        return 1
    else:
        return rfib(index-1) + rfib(index-2)
    
# print(rfib(100))
# print(rfib(1))
# print(rfib(0))

def recurfib(idx, a=0, b=1):
    if idx == 0:
        return a
    return recurfib(idx - 1, b, a + b)

print(recurfib(100))
print(recurfib(1))
print(recurfib(0))