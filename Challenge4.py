cache = {}


def fibonacciNumber(n):
    if n < 0:
        print(" -ve value not Fib")
        return
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:

        return fibonacciNumber(n - 2) + fibonacciNumber(n - 1)


for i in range(-2, 50):
    print("\t\t" + str(fibonacciNumber(i)), end=" ", flush=True)




