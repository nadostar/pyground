# coding: utf-8

import redis
import time
import threading

foods = [
    'Donut', 'Eclair', 'Froyo', 'Gingerbread', 'Honeycomb',
    'Ice Cream Sadwich', 'Jelly Bean', 'KitKat'
]

animals = [
    'Tiger', 'Leopard', 'SnowLeopard', 'Lion',
    'Mountain Lion', 'Mavericks'
]

end_of_message = b'__EOM__'

client = redis.StrictRedis()


def publisher(channel, message):
    time.sleep(1)

    for m in message:
        client.publish(channel, m)
        time.sleep(1)

    client.publish(channel, end_of_message)


def run_pubsub():
    threading.Thread(target=publisher,
                     args=('channel:food', foods,)).start()

    threading.Thread(target=publisher,
                     args=('channel:animal', animals)).start()

    pubsub = client.pubsub()

    pubsub.psubscribe(['channel*'])

    channels = 2  # 채널 수
    for item in pubsub.listen():
        print(item)
        if not channels:
            break

        if item['data'] == end_of_message:
            pubsub.unsubscribe(item['channel'])
            channels -= 1


if __name__ == '__main__':
    run_pubsub()
