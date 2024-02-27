def my_decorator(func):
    def header_footer():
        print('********   Nishant Python learning time   ***************\n')
        func()
        print('\n**************** BY FOR NOW************************')
    return header_footer


@my_decorator
def hello():
    print('Today I learnt about decorator, higher order function')

print(hello())
