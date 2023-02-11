import unittest

from child_credit import produceReport
from child import Child

class ChildCreditUnitTests(unittest.TestCase):

    # all unit tests begin with "test"
    def test_report_001(self):
        tom = Child("Tommy", 14)
        dick = Child("Richard", 12)
        harry = Child("Harold", 21)
        testVals = [tom, dick, harry]
        expectedOutput = 1500
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_report_002(self):
        testVals = [Child("A", 10), Child("B", 12), Child("C", 14), Child("D", 16), Child("E", 18), Child("E", 20)]
        expectedOutput = 2500
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_report_003(self):
        testVals = [Child("A", 19), Child("B", 19), Child("C", 21)]
        expectedOutput = 0;
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_report_004(self):
        testVals = []
        expectedOutput = 0;
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_report_005(self):
        testVals = [Child("A", 5), Child("B", 21)]
        expectedOutput = 1000;
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

    def test_report_006(self):
        testVals = [Child("A", 8), Child("B", 5), Child("C", 3), Child("D", 21)]
        expectedOutput = 2000;
        actualOutput = produceReport(testVals)
        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__':
    #buffer=True suppresses stdout
    unittest.main(buffer=True)
