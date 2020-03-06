def fibonnaci(n):
    current, former = 1, 0
    if n == 0:
        print(0)
    for i in range(n - 1):
        current, former = former, current + former

        print(current)

fibonnaci(13)
# fibonnaci(7)
fibonnaci(0)


