import unittest

from yahtzee import Group, score, validate
from yahtzee import ones, twos, threes, fours, fives, sixes
from yahtzee import pair, three_of_kind, four_of_kind
from yahtzee import two_pairs, small_straight, large_straight
from yahtzee import full_house, yahtzee, chance


class ValidateTest(unittest.TestCase):

    def testValidate(self):
        self.assertEqual(
            validate('12345'),
            {Group(n, 1) for n in [1, 2, 3, 4, 5]}
        )
        self.assertEqual(
            validate('12121'),
            {Group(1, 3), Group(2, 2)}
        )

    def testValidateTooShortRaises(self):
        with self.assertRaises(ValueError):
            validate('1234')

    def testValidateTooLongRaises(self):
        with self.assertRaises(ValueError):
            validate('1234')

    def testValidadateBadCharRaises(self):
        with self.assertRaises(ValueError):
            validate('1234a')
        with self.assertRaises(ValueError):
            validate('12340')
        with self.assertRaises(ValueError):
            validate('12347')
            

class CategoryTest(unittest.TestCase):

    def testOnes(self):
        self.assertEqual(score('23456', ones), 0)
        self.assertEqual(score('12131', ones), 3)
        self.assertEqual(score('11111', ones), 5)

    def testTwos(self):
        self.assertEqual(score('13456', twos), 0)
        self.assertEqual(score('12225', twos), 6)
        self.assertEqual(score('22222', twos), 10)

    def testThrees(self):
        self.assertEqual(score('11256', threes), 0)
        self.assertEqual(score('13356', threes), 6)

    def testFours(self):
        self.assertEqual(score('13556', fours), 0)
        self.assertEqual(score('13446', fours), 8)

    def testFives(self):
        self.assertEqual(score('13446', fives), 0)
        self.assertEqual(score('13556', fives), 10)

    def testSixes(self):
        self.assertEqual(score('13445', sixes), 0)
        self.assertEqual(score('13466', sixes), 12)


    def testPair(self):
        self.assertEqual(score('12345', pair), 0)
        self.assertEqual(score('12234', pair), 4)
        self.assertEqual(score('12224', pair), 4)
        self.assertEqual(score('12222', pair), 4)
        self.assertEqual(score('22222', pair), 4)
        self.assertEqual(score('11224', pair), 4)
        self.assertEqual(score('11244', pair), 8)

    def testThreeOfAKind(self):
        self.assertEqual(score('22335', three_of_kind), 0)
        self.assertEqual(score('11134', three_of_kind), 3)
        self.assertEqual(score('12224', three_of_kind), 6)
        self.assertEqual(score('11444', three_of_kind), 12)

    def testFourOfAKind(self):
        self.assertEqual(score('22233', four_of_kind), 0)
        self.assertEqual(score('11114', four_of_kind), 4)
        self.assertEqual(score('22224', four_of_kind), 8)
        self.assertEqual(score('14444', four_of_kind), 16)


    def testTwoPairs(self):
        self.assertEqual(score('11234', two_pairs), 0)
        self.assertEqual(score('11114', two_pairs), 0)
        self.assertEqual(score('12345', two_pairs), 0)
        self.assertEqual(score('11234', two_pairs), 0)
        self.assertEqual(score('11224', two_pairs), 6)
        self.assertEqual(score('11244', two_pairs), 10)
        self.assertEqual(score('11144', two_pairs), 10)
        self.assertEqual(score('11444', two_pairs), 10)

    def testSmallStraight(self):
        self.assertEqual(score('54321', small_straight), 15)
        self.assertEqual(score('65432', small_straight), 0)

    def testLargeStraight(self):
        self.assertEqual(score('54321', large_straight), 0)
        self.assertEqual(score('65432', large_straight), 20)


    def testFullHouse(self):
        self.assertEqual(score('11112', full_house), 0)
        self.assertEqual(score('11123', full_house), 0)
        self.assertEqual(score('11223', full_house), 0)
        self.assertEqual(score('11233', full_house), 0)

        self.assertEqual(score('11133', full_house), 9)
        self.assertEqual(score('66555', full_house), 27)

        self.assertEqual(score('44444', full_house), 0)

    def testYahtzee(self):
        self.assertEqual(score('11112', yahtzee), 0)
        self.assertEqual(score('11111', yahtzee), 50)
        self.assertEqual(score('66665', yahtzee), 0)
        self.assertEqual(score('66666', yahtzee), 50)

    def testChance(self):
        self.assertEqual(score('11112', chance), 6)
        self.assertEqual(score('66666', chance), 30)

