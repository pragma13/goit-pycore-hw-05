# returns fibonacci function that calculates fibonacci number
# results are stored in cache dictionary to avoid duplicate calculations
def caching_fibonacci():
    cached_fibonacci_dict = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cached_fibonacci_dict:
            return cached_fibonacci_dict[n]

        # calculate recursively and save result to cache
        cached_fibonacci_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cached_fibonacci_dict[n]

    return fibonacci


fib = caching_fibonacci()


print(fib(10))
print(fib(15))
print(fib(0))
print(fib(-100))
print(fib(15))
print(fib(7))
