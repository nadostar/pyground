import sys

from blinker import Signal


signal = Signal('disconnect_signal')


@signal.connect_via(Signal.ANY)
def receive_data(sender, **kw):
    print("Caught strong signal from : {}, data: {}".format(sender, kw))
    return "test"


@signal.connect_via(Signal.ANY)
def receive_data2(sender, **kw):
    print("Caught signal2 from : {}, data: {}".format(sender, kw))
    return "received2"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'disconnect':
        signal.disconnect(receive_data, Signal.ANY)
    result = signal.send('anonymous', abc=123)
    print(result)
