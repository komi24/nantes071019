# -*- coding: utf-8 -*-

import unittest
from Compte import Compte


class TestRetraitCompte(unittest.TestCase):
    def setUp(self):
        self.compte = Compte(5000)
    def testBasicRetrait(self):
        self.compte.retrait(100)
        self.assertEqual(self.compte.solde, 4900)
    def testBasicRetrait2(self):
        self.compte.retrait(100)
        self.assertEqual(self.compte.solde, 4900)
    def testNegativeRetrait(self):
        with self.assertRaises(AssertionError):
            self.compte.retrait(-100)
        
    