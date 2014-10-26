def fib2(n):
    fibList=[1]
    a, b=1, 1
    while b<=n:
        fibList.append(b)
        a,b=b,a+b
    return fibList
req=int(input("max num: "))
print(fib2(req))
