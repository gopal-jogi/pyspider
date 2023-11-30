def outer(func):
    def inner():
        print('-'*20)
        func()
        print('-'*20)
    return inner
@outer
def abs():
    print('    Hello Word')

abs()