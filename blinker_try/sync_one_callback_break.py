# coding: utf-8

from blinker import signal

channel = signal('channel')


@channel.connect
def receive(sender, **kwargs):
    print('[receive] channel from : {}, data:{}'.format(sender, kwargs))
    test = 1 / 0
    return test


@channel.connect
def receive2(sender, **kwargs):
    print('[receive2] channel from : {}, data:{}'.format(sender, kwargs))
    return 'received'


if __name__ == '__main__':
    rv = channel.send('anonymous', message='I feel it coming')
    print(rv)
