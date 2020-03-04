"""
12)Logger Decorator:
https://www.getoutline.com/share/63c5692f-51bb-4770-8047-566fac38bb95
"""



def myDecorator(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}{args, kwargs}')
        a = func(*args, **kwargs)
        print(f'Finished {func.__name__}({a})')
    return wrapper
    
@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print("argument a: ", a)
    print("argument b: ", b)
    print("argument args: ", args)
    print("argument kwargs: ", kwargs)
    return a + b


testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)