import unittest

from metafun.lang import is_concrete, eval_rule, ctx


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

    def test_eval_digit(self):
        from metafun.obj.digit import Digit

        target = list(map(lambda x: Digit(x), [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]))
        test = eval_rule(0, ctx, 'metafun.obj.digit.Digit')
        self.assertListEqual(target, test)

    def test_eval_generic_list(self):
        from metafun.obj.digit import Digit
        from metafun.lang.list import List

        result = eval_rule(0, ctx, 'metafun.lang.list.List[metafun.obj.digit.Digit]')
        print(result)


if __name__ == "__main__":
    unittest.main()
