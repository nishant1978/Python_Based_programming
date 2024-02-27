# High order function are the functions which are passed a parameter or as return function
#examples could be map, reduce, filter

def hello(func):
    func()

def greet():
    print('hellooo')

#print(hello(greet))

def wish():
    def func():
        return 5
    return func()

print(wish())