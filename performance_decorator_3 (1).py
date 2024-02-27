from time import time #This is called module

def performance(func):
    def measure(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'The total duration of the function call is {t2 - t1} ms')
        return func
    return measure

@performance
def calculate():
    for i in range(100000000):
        i*5

calculate()