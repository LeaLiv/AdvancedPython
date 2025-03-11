import time
def time_decorator(func):
    def inner(*args):
        # Calculate the start time
        start = time.time()
        result=func(*args)
        # Calculate the end time and time taken
        end = time.time()
        length = end - start
        # Show the results : this can be altered however you like
        print("It took", length, "seconds!")
        return result
    return inner

@time_decorator
def func1():
    for i in range(10):
        for j in range(10):
            print(f'i: {i} j: {j}')

@time_decorator
def func2():
    for _ in range(13):
        print(10*8+5)
func1()
func2()

cache_dict={}
def cache_decorator(func):
    #if this is the first run of the function
    def inner(*args):
        if args in cache_dict:
            return cache_dict[args]
        x=func(*args)
        cache_dict[args]=x
        return x
    return inner

@time_decorator
@cache_decorator
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(fibonacci(1000))
print(fibonacci(101))
print(fibonacci(1000))