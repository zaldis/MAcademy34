import unittest

from .solver import solve


class TestRebusSolve(unittest.TestCase):

    def test_front_removing(self):
        pattern = "''abcd"

        answer = solve(pattern)

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


    def test_no_removing(self):
        pattern = "abcd"

        answer = solve(pattern)

        self.assertEqual(answer, 'abcd')

    def test_front_and_back_removing(self):
        patter = "''abcde''"

        answer = solve(patter)

        self.assertEqual(answer, 'c')


if __name__ == '__main__':
    unittest.main()