import unittest

from metafun.obj.letter import Letter
from metafun.lang import generate


class TestLetter(unittest.TestCase):

    def test_gen(self):
        target = list(map(lambda x: Letter(x), [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        ]))
        test = list(generate(Letter))
        self.assertListEqual(target, test)


if __name__ == "__main__":
    unittest.main()
