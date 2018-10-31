def factorial(a):
    b=1
    for i in range(a):
        b = a*b
        a = a-1
    print(b)

factorial(15)
