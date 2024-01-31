
import sys
import unittest
import random
from searching import linear_search, binary_recursive_search, binary_search

sys.setrecursionlimit(1000000)


class TestSearching(unittest.TestCase):
    FOUND_STATUS = True
    NOT_FOUND_STATUS = False
    NOT_FOUND_INDEX = -1

    def test_edge_case_linear_search(self) -> None:
        status, index = linear_search([], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = linear_search([1], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = linear_search([1], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)

        status, index = linear_search([1, 3], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)
        status, index = linear_search([1, 3], 3)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 1)

    def test_edge_case_binary(self) -> None:
        status, index = binary_search([], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = binary_search([1], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = binary_search([1], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)

        status, index = binary_search([1, 3], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)
        status, index = binary_search([1, 3], 3)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 1)

    def test_edge_case_binary_recursive(self) -> None:
        status, index = binary_recursive_search([], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = binary_recursive_search([1], 3)
        self.assertEqual(status, self.NOT_FOUND_STATUS)
        self.assertEqual(index, self.NOT_FOUND_INDEX)

        status, index = binary_recursive_search([1], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)

        status, index = binary_recursive_search([1, 3], 1)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 0)
        status, index = binary_recursive_search([1, 3], 3)
        self.assertEqual(status, self.FOUND_STATUS)
        self.assertEqual(index, 1)

    def generate_list(self, sample_size: int, ordered: bool = False) -> tuple[list[int], int, int]:
        list_random_ints = random.sample(range(1, 100000 + 1), sample_size)
        if ordered:
            list_random_ints.sort()
        key = random.choice(list_random_ints)
        index = list_random_ints.index(key)
        return (list_random_ints, key, index)

    def test_results_linear_search(self) -> None:
        sample_size = 10
        while sample_size < 100000:
            list_random_ints, key, index = self.generate_list(sample_size)

            status, _index = linear_search(list_random_ints, key)
            self.assertEqual(status, self.FOUND_STATUS)
            self.assertEqual(index, _index)

            status, _index = linear_search(
                list_random_ints, random.randint(100000+5, 100000*5))
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            status, _index = linear_search(list_random_ints, -5)
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            sample_size += 1000

    def test_results_binary_search(self) -> None:
        sample_size = 10
        while sample_size < 100000:
            list_random_ints, key, index = self.generate_list(
                sample_size,
                ordered=True
            )

            status, _index = binary_search(list_random_ints, key)
            self.assertEqual(status, self.FOUND_STATUS)
            self.assertEqual(index, _index)

            status, _index = binary_search(
                list_random_ints,
                random.randint(100000+5, 100000*5)
            )
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            status, _index = binary_search(list_random_ints, -5)
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            sample_size += 1000

    def test_results_binary_recursive_search(self) -> None:
        sample_size = 10
        while sample_size < 100000:
            list_random_ints, key, index = self.generate_list(
                sample_size,
                ordered=True
            )

            status, _index = binary_recursive_search(list_random_ints, key)
            self.assertEqual(status, self.FOUND_STATUS)
            self.assertEqual(index, _index)

            status, _index = binary_recursive_search(
                list_random_ints,
                random.randint(100000+5, 100000*5)
            )
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            status, _index = binary_recursive_search(list_random_ints, -5)
            self.assertEqual(status, self.NOT_FOUND_STATUS)
            self.assertEqual(self.NOT_FOUND_INDEX, _index)

            sample_size += 1000