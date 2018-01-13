#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = ''
    while True:
        print('start')
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

# c = consumer()
# produce(c)
# def yieldtest(xx):
#     print ('before')
#     x=yield xx
#     print x
# zz = yieldtest(2)
# print('center')
# for i in zz:
#     print('for %s' %i)
def test():
    print ('test1:')
    x=yield 1

def test2():
    print ('3')
    for i in (yield ()):
        print i
for i in test2():
    print (i)