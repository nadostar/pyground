# coding: utf-8

from blinker import Signal


class AltProcessor(object):
    on_ready = Signal()
    on_complete = Signal()

    def __init__(self, name):
        self.name = name

    def go(self):
        self.on_ready.send(self)
        print('Alternate processing...')
        self.on_complete.send(self)

    def __repr__(self):
        return "<AltProcessor {}>".format(self.name)


apc = AltProcessor('Hello')


@apc.on_complete.connect
def completed(sender):
    print("Altprocess: {} completed".format(sender))


if __name__ == '__main__':
    apc.go()
