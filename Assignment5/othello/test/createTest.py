'''
     Created on Mar 8, 2020
     Tests for the create.py program
'''
import unittest
import othello.create as c

class Test(unittest.TestCase):

    def testHappyPaths(self):
        # Happy path data to be tested
        happyPath1 = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 6, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        'tokens': {'light': 6, 'dark': 5, 'blank': 1},
                        'status': 'ok',
                        'integrity': 'd0f18c5b412ab1dbf89da19baa33cc35f4a7dd0619ce7b7dcb2381d2cb14a412'}
        happyPath2 = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 9, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        'tokens': {'light': 9, 'dark': 5, 'blank': 1},
                        'status': 'ok',
                        'integrity': '723c769319c6529cf8520336232a9e5d281be77df1455c6ceb10a5d1d4733236'}
        happyPath3 = {'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 0, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        'tokens': {'light': 0, 'dark': 5, 'blank': 1},
                        'status': 'ok',
                        'integrity': '4bd2efa7e0d5f13551f7277950e45b6fcfe7d5159b80823a5dcbdf57abb4d83a'}
        happyPath4 = {'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                3, 3, 3, 3, 3, 3, 3, 1, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                                3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        'tokens': {'light': 1, 'dark': 5, 'blank': 3},
                        'status': 'ok',
                        'integrity': 'f211a92f576794a821bb24f359739b8b42a6a16634005a1e4b32313a6575e2be'}
        happyPath5 = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 3, 9, 4, 4, 4, 4, 4, 4, 4, 4, 9, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        'tokens': {'light': 3, 'dark': 9, 'blank': 4},
                        'status': 'ok',
                        'integrity': 'a3718ffbc2f822320ee4db10c269a9749859b9952db13ff6b289a6ebd6ce42c6'}
        happyPath6 = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 3, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        'tokens': {'light': 3, 'dark': 0, 'blank': 4},
                        'status': 'ok',
                        'integrity': '7bf98e8385a158097f52361dac139bb5882f3eaa48e8146d72d65de5981d2e5e'}
        happyPath7 = {'board': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 3, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        'tokens': {'light': 3, 'dark': 2, 'blank': 4},
                        'status': 'ok',
                        'integrity': '71f91a7d487c9e9ad69a43269c6a90c449f97fd93848b8493e47a2f6054e7c82'}
        happyPath8 = {'board': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 3, 4, 9, 9, 9, 9, 9, 9, 9, 9, 4, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                        'tokens': {'light': 3, 'dark': 4, 'blank': 9},
                        'status': 'ok',
                        'integrity': '5b4c82af0cf6a72ab1938b8e5a3c1ce413b9db583d0f974703954427413021d0'}
        happyPath9 = {'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'tokens': {'light': 3, 'dark': 4, 'blank': 0},
                        'status': 'ok',
                        'integrity': 'eeaa1d4229234a1453901319e7f584a337595d6d332a22a76c4aae8888cde9d6'}
        happyPath10 = {'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                                 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                        'status': 'ok',
                        'integrity': '682b1bac788017f23b846862ce44f2c3efe03a22f49de36085e0e57fc6957416'}
        happyPath11 = {'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                        'status': 'ok',
                        'integrity': 'b87b212e557d1dc1080f1c6e380bab404ae8cffa048b86e649e54c620f0d9c6a'}
        happyPath12 = {'board': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 4, 5, 5, 5, 5, 5, 5, 4, 3,
                                5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        'tokens': {'light': 3, 'dark': 4, 'blank': 5},
                        'status': 'ok',
                        'integrity': '306a2474c8f8b41c9e31af0fe360f9fcaf3531b3b4a1c3624acd8fbc2530b02e'}
        happyPath13 = {'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        'tokens': {'light': 1, 'dark': 2, 'blank': 0},
                        'status': 'ok',
                        'integrity': 'b11fcf5f9ac9d3b8cea8085208e210182a8d6b73a84028562ab2c87d190b9ada'}
        
        # Happy path unit tests
        self.assertEqual(c._create({'light': 6, 'dark': 5, 'blank': 1, 'size': 10}), happyPath1)  # Happy path test 010: nominal light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 9, 'dark': 5, 'blank': 1, 'size': 10}), happyPath2)  # Happy path test 020: high bound light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 0, 'dark': 5, 'blank': 1, 'size': 10}), happyPath3)  # Happy path test 021: low bound light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'dark': 5, 'blank': 3, 'size': 10}), happyPath4)              # Happy path test 022: missing light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 9, 'blank': 4, 'size': 10}), happyPath5)  # Happy path test 030: nominal light, high bound dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 0, 'blank': 4, 'size': 10}), happyPath6)  # Happy path test 031: nominal light, low bound dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 3, 'blank': 4, 'size': 10}), happyPath7)             # Happy path test 032: nominal light, missing dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'blank': 9, 'size': 10}), happyPath8)  # Happy path test 040: nominal light, nominal dark, high bound blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'blank': 0, 'size': 10}), happyPath9)  # Happy path test 041: nominal light, nominal dark, low bound blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'size': 10}), happyPath9)              # Happy path test 042: nominal light, nominal dark, missing blank, nominal size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'blank': 5, 'size': 16}), happyPath10) # Happy path test 050: nominal light, nominal dark, nominal blank, high bound size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'blank': 5, 'size': 6}), happyPath11)  # Happy path test 051: nominal light, nominal dark, nominal blank, low bound size
        self.assertEqual(c._create({'light': 3, 'dark': 4, 'blank': 5}), happyPath12)             # Happy path test 052: nominal light, nominal dark, nominal blank, missing size
        self.assertEqual(c._create({}), happyPath13)                                              # Happy path test 060: missing light, missing dark, missing blank, missing size
        pass

    def testSadPaths(self):
        # Sad path data to be tested
        sadPath1 = {'status': 'error: one of the parameters is out of the specified bounds'}
        sadPath2 = {'status': 'error: one of the parameters is not an integer'}
        sadPath3 = {'status': 'error: one of the parameters was passed a null value'}
        sadPath4 = {'status': 'error: the size parameter was passed an odd value'}
        sadPath5 = {'status': 'error: the light, dark and blank parameters have a value in common'}
        
        # Sad path unit tests
        self.assertEqual(c._create({'light': 10}), sadPath1)                       # Sad path test 900: above bound light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': -1}), sadPath1)                       # Sad path test 901: below bound light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': 'w'}), sadPath2)                      # Sad path test 902: non-integer light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'light': None}), sadPath3)                     # Sad path test 903: null light, nominal dark, nominal blank, nominal size
        self.assertEqual(c._create({'dark': 10}), sadPath1)                        # Sad path test 910: nominal light, above bound dark, nominal blank, nominal size
        self.assertEqual(c._create({'dark': -1}), sadPath1)                        # Sad path test 911: nominal light, below bound dark, nominal blank, nominal size
        self.assertEqual(c._create({'dark': 'd'}), sadPath2)                       # Sad path test 912: nominal light, non-integer dark, nominal blank, nominal size
        self.assertEqual(c._create({'dark': None}), sadPath3)                      # Sad path test 913: nominal light, null dark, nominal blank, nominal size
        self.assertEqual(c._create({'blank': 10}), sadPath1)                       # Sad path test 920: nominal light, nominal dark, above bound blank, nominal size
        self.assertEqual(c._create({'blank': -1}), sadPath1)                       # Sad path test 921: nominal light, nominal dark, below bound blank, nominal size
        self.assertEqual(c._create({'blank': 'b'}), sadPath2)                      # Sad path test 922: nominal light, nominal dark, non-integer blank, nominal size
        self.assertEqual(c._create({'blank': None}), sadPath3)                     # Sad path test 923: nominal light, nominal dark, null blank, nominal size
        self.assertEqual(c._create({'size': 17}), sadPath1)                        # Sad path test 930: nominal light, nominal dark, nominal blank, above bound size
        self.assertEqual(c._create({'size': 5}), sadPath1)                         # Sad path test 931: nominal light, nominal dark, nominal blank, below bound size
        self.assertEqual(c._create({'size': 9}), sadPath4)                         # Sad path test 932: nominal light, nominal dark, nominal blank, odd size
        self.assertEqual(c._create({'size': 1.2}), sadPath2)                       # Sad path test 933: nominal light, nominal dark, nominal blank, non-integer size
        self.assertEqual(c._create({'size': None}), sadPath3)                      # Sad path test 934: nominal light, nominal dark, nominal blank, null size
        self.assertEqual(c._create({'light': 5, 'dark': 5, 'blank': 0}), sadPath5) # Sad path test 940: nominal light, dark = light, nominal blank, nominal size
        self.assertEqual(c._create({'light': 5, 'dark': 2, 'blank': 5}), sadPath5) # Sad path test 941: nominal light, nominal dark, blank = light, nominal size
        self.assertEqual(c._create({'light': 1, 'dark': 2, 'blank': 2}), sadPath5) # Sad path test 942: nominal light, nominal dark, blank = dark, nominal size
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()