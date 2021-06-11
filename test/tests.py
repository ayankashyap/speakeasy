import unittest

from speakeasy.convert import SpeakEasyConvertor


class Tester(unittest.TestCase):
    convertor = SpeakEasyConvertor()

    def test_numbers(self):
        txt = "sixty million five hundred thousand fifty"
        result = "60500050"
        self.assertEqual(self.convertor.convert(txt), result)

    def test_abbreviations(self):
        txt = "H T M L"
        result = "HTML"
        self.assertEqual(self.convertor.convert(txt), result)

    def test_quantifiers(self):
        txt = "Quadruple H"
        result = "HHHH"
        self.assertEqual(self.convertor.convert(txt), result)

    def test_complete(self):
        txt = "I and my friend triple H bought sixty thousand five hundred and fifty six dollars worth of apples " \
              "at S F M L "
        result = "I and my friend HHH bought $60556 worth of apples at SFML"
        self.assertEqual(self.convertor.convert(txt), result)


if __name__ == "__main__":
    unittest.main()
