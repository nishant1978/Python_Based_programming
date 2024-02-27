#generator is faster in performance
#yield keyword leads to lesser memory

def generate_num(num):
    for i in range(num):
        yield i * 2

#for item in generate_num(100):
#    print(item)

n = generate_num(10)
next(n)
print(next(n))
