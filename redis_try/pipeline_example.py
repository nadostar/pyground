# coding: utf-8
"""
Redis Pipeline and Transaction(Multi/Exec)

Pipeline (ex: 대용량 데이터 입력) 을 이용하면 성능은 좋아지는데,
Redis는 Single Thread 라, pipeline 으로 처리하는 동안에는 다른 client의 작어을 처리하지 못하게 되는거 아닌가요?

결론부터 내리자면, pipeline 형태로 데이터를 전달하더라도 중간에 command를 수행 할 수 있다.

https://charsyam.wordpress.com/2013/12/31/redis-pipeline-and-transactionmultiexec/
"""

import multiprocessing
import redis
import random
import string

client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


def gen_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


data = gen_id(512)


def f(idx):
    print('PR', idx)

    with client.pipeline() as pipe:
        for i in range(idx * 1024 * 1024 * 2, (idx+1)*1024*1024 * 2):
            key = 'PR:{}'.format(i)
            pipe.get(key)
