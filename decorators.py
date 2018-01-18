# Decorators


def decorator_function(function):
    def decorator(*args, **kwargs):
        print("Decorater exceuted first {}".format(function.__name__))
        return function(*args, **kwargs)
    return decorator


# Method 1
def welcome():
    print("Hey Welcome")

decorator_welcome = decorator_function(welcome)
decorator_welcome()


#Method 2
@decorator_function
def welcome1():
    print("Hey Welcome 1")

welcome1()


#Example with parameter passing in function
@decorator_function
def user_info(firstname, lastname):
    print('My name is {}, {}'.format(firstname, lastname))

user_info('Supriya', 'Kanchan')


#Example using decorator in call
class decorator_class(object):

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("Call method exceuted first {}".format(self.function.__name__))
        return self.function(*args, **kwargs)


@decorator_class
def user_info(firstname, lastname):
    print('My name is {}, {}'.format(firstname, lastname))

user_info('Supriya', 'Kanchan')


