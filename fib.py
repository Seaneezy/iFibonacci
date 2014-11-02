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

def fib2(n):
    fibList=[1]
    #create a list with basic value 1
    #starting values for a and b
    a, b=1, 1
    #while the length of the list is less than the requested amt
    while len(fibList) < n:
        #append b
        fibList.append(b)
        #shift up numbers
        a,b=b,a+b
        #return list of numbers in sequence.
    return fibList
"""
n=4 any value for n.
print(fib2(n))

x=int(input("max num: "))
print(fib1(x))
"""

