import unittest

from dynamicProgramming import coinFlipping


class TestCoinFlipping(unittest.TestCase):


    def setUp(self):
        pass


    def test_ComputeMinimalCoins(self):
        twentySixCentsInWallet = 26
        walletOneminimalCoins = 2
        minimalCoinReturn = coinFlipping(twentySixCentsInWallet)
        self.assertEqual(minimalCoinReturn, walletOneminimalCoins)                

    
    def test_HandleEmptyCoin(self):

        zeroCentsInWallet = emptyWalletMinimalCoins = 0    
        minimalCoinReturn = coinFlipping(zeroCentsInWallet)
        self.assertEqual(minimalCoinReturn, emptyWalletMinimalCoins)


    def test_HandleNegativeChange(self):

        negativeWalletChange = -24
        expectedError = 0
        minimalCoinReturn = coinFlipping(negativeWalletChange)
        self.assertEqual(minimalCoinReturn, expectedError)