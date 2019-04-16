def add(a,b):
    return a+b


def decor(func):
    def wrapper(a, b):
        print("checking.......")
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            return "Data should be integer"
    return wrapper

add = decor(add)
print(add(1, '2'))
print(add(1, 2))

""""""""""""""""""""""""


def hello_world():
    print("printing hello world")
    # return "printing hello world"


def decor1(func):
    def wrapper():
        print("++++")
        func()
        # return func()
        print("****")
    return wrapper

hello_world = decor1(hello_world)
hello_world()
# print(hello_world())

"""using pie syntax"""


def decor2(fun):
    def wrapper(a, b):
        if a != 'hello' and b != 'world':
            return fun(a, b)
        else:
            return "String should not contain hello and world"
    return wrapper


@decor2
def helloworldcheck(a,b):
    return '{} and {} etc'.format(a,b)

abc = helloworldcheck('hello', 'world')
print(abc)
xyz = helloworldcheck('supriya', 'kanchan')
print(xyz)

