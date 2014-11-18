from unittest import TestCase
from syncify import syncify
import time


def asyncFunction(number, callback=None):
    time.sleep(1)
    if callback:
        callback(number * 10)

def asyncFunction2(number1, number2, after=None):
    time.sleep(1)
    if after:
        after(number1 * 10, number2*10)

class TestSyncify(TestCase):
    def test_syncify1(self):
        ten = syncify(asyncFunction)(1)
        self.assertTrue(ten == 10)
    def test_syncify2(self):
        ten, hundred = syncify(asyncFunction2, kw='after')(1, 10)
        self.assertTrue(ten == 10 and hundred == 100)
