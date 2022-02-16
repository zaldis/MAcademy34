from unittest import TestCase

from .solver import solve


class TestRebusSolve(TestCase):

    def test_front_removing(self):
        # arrange
        pattern = "''abcd"

        # act
        answer = solve(pattern)

        # assert
        self.assertEqual(answer, 'cd')

    def test_back_removing(self):
        pattern = "abcd''"
        answer = solve(pattern)
        self.assertEqual(answer, 'ab')

    def test_front_total_removing(self):
        pattern = "''''abcd"
        answer = solve(pattern)
        self.assertEqual(answer, '')

    def test_back_total_removing(self):
        pattern = "abcd''''"
        answer = solve(pattern)
        self.assertEqual(answer, '')

    def test_front_and_back_removing(self):
        pattern = "''abcde''"
        answer = solve(pattern)
        self.assertEqual(answer, 'c')

    def test_no_removing(self):
        pattern = "abcd"
        answer = solve(pattern)
        self.assertEqual(answer, 'abcd')
