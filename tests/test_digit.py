import unittest

from metafun.obj.digit import Digit
from metafun.lang import generate


class TestLetter(unittest.TestCase):

    def test_gen(self):
        target = list(map(lambda x: Digit(x), [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]))
        test = list(generate(Digit))
        self.assertListEqual(target, test)


if __name__ == "__main__":
    unittest.main()
