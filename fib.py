def fib(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        if n <= 0:
            print(0)
        elif n == 1:
            print(n1)
        else:
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
