# coding: utf-8

"""
"""

from blinker import signal


def subscriber(sender):
    print("Got a signal sent by '{}'".format(sender))


litener = signal('channel')
litener.connect(subscriber)

if __name__ == '__main__':
    commands = ['add', 'push', 'pop', 'channel', 'login']

    for command in commands:
        litener.send(command)
