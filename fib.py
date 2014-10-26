def fib1(n):
    fibList=[1]
    a, b=1, 1
    while b<=n:
        fibList.append(b)
        a,b=b,a+b
    return fibList
"""
x=int(input("max num: "))
print(fib2(x))
"""
