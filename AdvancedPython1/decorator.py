import time
def time_decorator(func):
    def inner():
        # Calculate the start time
        start = time.time()
        func()
        # Calculate the end time and time taken
        end = time.time()
        length = end - start
        # Show the results : this can be altered however you like
        print("It took", length, "seconds!")
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

