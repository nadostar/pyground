# coding: utf-8


class Person(object):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Simon')
p.say_hi()
# Person().say_hi()
