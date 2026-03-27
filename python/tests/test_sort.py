import random
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from ragesort import bit_radix_sort

class TestRageSort(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(bit_radix_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(bit_radix_sort([42]), [42])
        self.assertEqual(bit_radix_sort([-7]), [-7])
        self.assertEqual(bit_radix_sort([0]), [0])
    
    def test_already_sorted(self):
        data = [-100, -50, -10, 0, 5, 23, 100]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_reverse_sorted(self):
        data = [100, 23, 5, 0, -10, -50, -100]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_all_negative(self):
        data = [-1, -5, -2, -8, -3, -9, -4]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_all_positive(self):
        data = [7, 2, 9, 1, 5, 3, 8, 4, 6]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_with_zeros(self):
        data = [0, -1, 1, 0, -2, 2, 0]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_duplicates(self):
        data = [5, 3, 5, 1, 5, 3, 5, 1, 5]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_large_numbers(self):
        data = [2**31 - 1, -2**31, 0, 1234567, -7654321]
        self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_random_small(self):
        for _ in range(50):
            data = [random.randint(-100, 100) for _ in range(50)]
            self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_random_medium(self):
        for _ in range(20):
            data = [random.randint(-10**6, 10**6) for _ in range(500)]
            self.assertEqual(bit_radix_sort(data), sorted(data))
    
    def test_radix_bits_variants(self):
        data = [random.randint(-1000, 1000) for _ in range(200)]
        for bits in [4, 8, 12, 16]:
            with self.subTest(radix_bits=bits):
                self.assertEqual(bit_radix_sort(data, radix_bits=bits), sorted(data))

if __name__ == '__main__':
    unittest.main()