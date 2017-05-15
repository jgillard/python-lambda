import json
import pytest

from service import *


def read(path, loader=None):
    with open(path) as fh:
        if not loader:
            return fh.read()
        return loader(fh.read())


def test_add():
    assert(add(1, 1) == 2)
    assert(add(1, -1) == 0)


def test_handler():
    event = read('event.json', loader=json.loads)
    assert(handler(event, None) == pytest.approx(5.858))
