#Testing the backend
import unittest
from backend import helper

def test_short_array_1():
    array = [1]
    key = 0
    index = helper.binarySearch(array, key)
    assert index == [1,1]