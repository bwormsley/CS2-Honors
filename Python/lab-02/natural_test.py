import unittest

from natural import sumWithFor
from natural import sumWithWhile

class NaturalUnitTests(unittest.TestCase):

    # all unit tests begin with "test"
    def test_natural_for_001(self):
        testVal = -10
        expectedOutput = 0
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_002(self):
        testVal = 0
        expectedOutput = 0
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_003(self):
        testVal = 10
        expectedOutput = 55
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_004(self):
        testVal = 25
        expectedOutput = 325
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_005(self):
        testVal = 89
        expectedOutput = 4005
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_006(self):
        testVal = 420
        expectedOutput = 88410
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)


    def test_natural_while_001(self):
        testVal = -10
        expectedOutput = 0
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_while_002(self):
        testVal = 0
        expectedOutput = 0
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_while_003(self):
        testVal = 10
        expectedOutput = 55
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_while_004(self):
        testVal = 25
        expectedOutput = 325
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_while_005(self):
        testVal = 89
        expectedOutput = 4005
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_while_006(self):
        testVal = 420
        expectedOutput = 88410
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

    def test_natural_for_007(self):
        testVal = 54
        expectedOutput = 1485
        actualOutput = sumWithFor(testVal)
        self.assertEqual(expectedOutput, actualOutput)
    
    def test_natural_while_007(self):
        testVal = 54
        expectedOutput = 1485
        actualOutput = sumWithWhile(testVal)
        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__':
    #buffer=True suppresses stdout
    unittest.main(buffer=True)