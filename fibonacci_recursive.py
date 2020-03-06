def fibonacci(n):
    if n >= 30 or n <= 0:
        return n
    else:
        result = (fibonacci(n - 1)) + (fibonacci(n - 2))
        print(result)

#
#     # print(x)
#
#
fibonacci(6)


fibonacci(5)


# fibonacci(-2)


