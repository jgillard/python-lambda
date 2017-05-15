# -*- coding: utf-8 -*-


def add(x, y):
    return x + y


def handler(event, context):
    # Your code goes here!
    e = event.get('e')
    pi = event.get('pi')
    return add(e, pi)
