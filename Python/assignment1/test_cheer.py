import unittest

from cheer import huskerMavScore
from cheer import winner

class CheerUnitTests(unittest.TestCase):

    list01 = [2, 9, 4, 25, 57, 45, 53]
    list02 = [5, 3, 45, 10, 1, 2, 0, 4]
    list03 = [4, 11, 5, 17, 0, 34, 63]
    list04 = [12, 9, 25, 51, 3, 7, 44]
    list05 = [15, 3, 5, 17]
    list06 = [15, 75, 90, 30, 45]
    def test_score_001(self):
        expectedOutputA = 111
        expectedOutputB = 70
        (actualOutputA,actualOutputB) = huskerMavScore(self.list01)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_001(self):
        actualOutput = winner(self.list01)
        self.assertTrue( actualOutput < 0 )

    def test_score_002(self):
        expectedOutputA = 48
        expectedOutputB = 60
        (actualOutputA,actualOutputB) = huskerMavScore(self.list02)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_002(self):
        actualOutput = winner(self.list02)
        self.assertTrue( actualOutput > 0 )

    def test_score_003(self):
        expectedOutputA = 63
        expectedOutputB = 5
        (actualOutputA,actualOutputB) = huskerMavScore(self.list03)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_003(self):
        actualOutput = winner(self.list03)
        self.assertTrue( actualOutput < 0 )

    def test_score_004(self):
        expectedOutputA = 75
        expectedOutputB = 25
        (actualOutputA,actualOutputB) = huskerMavScore(self.list04)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_004(self):
        actualOutput = winner(self.list04)
        self.assertTrue( actualOutput < 0 )

    def test_score_005(self):
        expectedOutputA = 18
        expectedOutputB = 20
        (actualOutputA,actualOutputB) = huskerMavScore(self.list05)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_005(self):
        actualOutput = winner(self.list05)
        self.assertTrue( actualOutput > 0 )

    def test_score_006(self):
        expectedOutputA = 255
        expectedOutputB = 255
        (actualOutputA,actualOutputB) = huskerMavScore(self.list06)
        self.assertEqual(expectedOutputA, actualOutputA)
        self.assertEqual(expectedOutputB, actualOutputB)

    def test_winner_006(self):
        actualOutput = winner(self.list06)
        self.assertTrue( actualOutput >= 0 )

if __name__ == '__main__':
    #buffer=True suppresses stdout
    unittest.main(buffer=True)