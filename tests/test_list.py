import unittest

from itertools import product
from metafun.obj.digit import Digit
from metafun.lang.list import List
from metafun.lang import generate


class TestList(unittest.TestCase):

    def test_gen(self):
        digits = list(map(lambda x: Digit(x), [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]))
        digits0 = [[]]
        digits1 = list(map(lambda x: [x], digits))
        digits2 = list(map(list, product(digits, digits)))
        digits3 = list(map(list, product(digits, digits, digits)))
        digits4 = list(map(list, product(digits, digits, digits, digits)))
        target = digits0 + digits1 + digits2 + digits3 + digits4

        test = list(generate(List[Digit]))
        self.assertListEqual(target, test)


if __name__ == "__main__":
    unittest.main()
