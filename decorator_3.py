def my_decorator(func):
    def header_footer(*args, **kwargs):
        print('********   Nishant Python learning time   ***************\n')
        func(*args, **kwargs)
        print('\n**************** BY FOR NOW************************')
    return header_footer


@my_decorator
def hello(greetings, emoji, action):
    print(greetings, emoji, action)

print(hello('HareKrishna ', '😀', 'Coming for satsang'))
