import unittest

from metafun.lang import is_concrete


class TestType(unittest.TestCase):

    def test_contrete_check(self):
        from metafun.obj.digit import Digit
        from metafun.lang.list import List

        test = is_concrete('T')
        self.assertTrue(test)

        test = is_concrete('[T]')
        self.assertFalse(test)

        test = is_concrete('List[T]')
        self.assertFalse(test)

        test = is_concrete('metafun.obj.digit.Digit')
        self.assertTrue(test)

        test = is_concrete('List[metafun.obj.digit.Digit]')
        self.assertTrue(test)

        test = is_concrete('[metafun.obj.digit.Digit, metafun.obj.digit.Digit]')
        self.assertTrue(test)

        test = is_concrete('[metafun.obj.digit.Digit, List[metafun.obj.digit.Digit]]')
        self.assertTrue(test)

        test = is_concrete('[List[T], List[metafun.obj.digit.Digit]]')
        self.assertFalse(test)

        test = is_concrete('[T, T]')
        self.assertFalse(test)

        test = is_concrete('[T, List[metafun.obj.digit.Digit]]')
        self.assertFalse(test)


if __name__ == "__main__":
    unittest.main()
