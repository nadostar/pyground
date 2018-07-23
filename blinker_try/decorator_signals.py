# coding: utf-8

"""
"""

import time
from blinker import signal

channel = signal('channel')


@channel.connect
def receive(sender, **kwargs):
    print("channel signal from: {}, data:{}".format(sender, kwargs))
    time.sleep(5)
    return 'received'


@channel.connect
def receive2(sender, **kwargs):
    print("channel signal2 from: {}, data:{}".format(sender, kwargs))
    return 'received2'


if __name__ == '__main__':
    rv = channel.send('anonymous', message='login')
    print(rv)
