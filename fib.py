def fib1(n):
    fibList=[1]
    #starting values for a and b
    a, b=1, 1
    #while the 2nd number is less than or equal to requested value
    while b<=n:
        #append the 2nd number
        fibList.append(b)
        #shift a and b up the sequence
        a,b=b,a+b
        #return list of numbers in sequence
    return fibList
"""
x=int(input("max num: "))
print(fib1(x))
"""

