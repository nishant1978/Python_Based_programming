def fibo_using_List(num):
    a = 0
    b = 1
    result = [] # using LIST

    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fibo_using_List(10))
