"""
def c_to_f(c):
    return c * 9 / 5 + 32

assert c_to_f(100) == 212
assert c_to_f(0) == 32
assert c_to_f(-40) == -40
"""
"""
def compute_fact(N):
    if N < 0:
        assert N >= 0, "N must be non-negative"
    elif N == 0 or N == 1:
        return 1
    return N * compute_fact(N-1)

assert compute_fact(0) == 1
assert compute_fact(1) == 1
"""

"""
import unittest

def list_sum(A,N):
    total = 0
    for i in range(N):
        total += A[i]
    return total

class TestListSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(list_sum([1, 2, 3, 4], 4), 10)
"""
"""
def fibonacci(N):
    if N == 0:
        return 0
    fold = 1
    fcurr = 1
    for i in range(N):
        fnew = fcurr + fold
        fold, fcurr = fcurr, fnew
    return fnew
"""

def selection_sort(my_list):
    for i in range(len(my_list)):
        min_val = my_list[i]
        min_index = i
        for j in range(i, len(my_list)):
            if min_val > my_list[j]
