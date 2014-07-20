def fib(n):
     f1, f2 = 0, 1
     while f2 < n:
         print f2,
         f1, f2 = f2, f1 + f2
fib(10)
