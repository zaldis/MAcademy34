def lesson1(name=None):
    # if name == 'correct':
    #     return True
    # else:
    #     return False

    # if name == 'correct':
    #     return True
    # return False

    return name == 'correct'


class Demo(object):
    
    def __init__(self):
        super().__init__()

    @classmethod
    def say_hello(cls):
        print('hello')

    def my_method(self):
        self.say_hello()
        Demo.say_hello()
