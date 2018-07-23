# coding: utf-8

"""
redis pub / sub 기능

Pub/Sub System 과 Message Queue는 다른 것이다.
Pub/Sub System 은 현재 채널에 가입한 Subscriber 들 모두에게 특정 이벤트를 전달하는 것이다.
MQ는 보통 일반적으로 작업을 큐잉하고 있다가 요청하는 곳에 데이터를 전달하기 위해서 보관하는 시스템 이다.

https://charsyam.wordpress.com/page/14/
https://github.com/antirez/redis/issues/998
"""

import redis
import time
import threading

CHANNEL_NAME = 'channel:word'

message = "You play with the cards you're dealt... Whatever that means."
end_of_message = b'__EOM__'

client = redis.StrictRedis()


def publisher(message):
    time.sleep(1)
    for m in message:
        client.publish(CHANNEL_NAME, m)
        time.sleep(1)

    client.publish(CHANNEL_NAME, end_of_message)


def run_pubsub():
    threading.Thread(target=publisher,
                     args=(message.split(),)).start()

    pubsub = client.pubsub()
    pubsub.subscribe(CHANNEL_NAME)

    recv_msg = True
    for item in pubsub.listen():
        print(item)
        if not recv_msg:
            break

        if item['data'] == end_of_message:
            pubsub.unsubscribe()
            recv_msg = False


if __name__ == '__main__':
    run_pubsub()
