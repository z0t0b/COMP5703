'''
     Created on Mar 8, 2020
     Tests for the status.py program
'''
import unittest
import othello.status as s

class Test(unittest.TestCase):

        def testHappyPaths(self):
            # Happy path data to be tested
            happyPath1 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
            happyPath2 = {'light': 9, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 2, 0, 0, 0, 0, 2, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '5ab81cb67067273363db989119448a0b878896f7db5c268a50c4ae3062cb3647'}
            happyPath3 = {'light': 0, 'dark': 2, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': '1b7e612b959852acbaf6b55d3f6b8dab2cdc32248a58a89dcf022ae80e5b36de'}
            happyPath4 = {'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'}
            happyPath5 = {'light': 5, 'dark': 0, 'blank': 9,
                            'board': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 0, 9, 9, 9, 9, 0, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                            'integrity': '85c972c79b667135f99ad9380f4af4a7495c5b5de3768c9cb36c4bc73f0da08a'}
            happyPath6 = {'light': 5, 'dark': 9, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 9, 3, 3, 3, 3, 9, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '34932b7f4bbafed18cf99e367e29407e6aae8b49b2ced711f31e429e7efc2a12'}
            happyPath7 = {'light': 5, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 2, 3, 3, 3, 3, 2, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'a348c2dae89e65378fc64d889b1d394819c021b2e4cccb37310bbef9335bb900'}
            happyPath8 = {'light': 5, 'dark': 6, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'}
            happyPath9 = {'light': 5, 'dark': 6, 'blank': 9,
                            'board': [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 6, 9, 9, 9, 9, 6, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                            'integrity': '5b698f38d9d1c1754df196ee688f3900ceba9d074cb74b5e17c19a197b69bf02'}
            happyPath10 = {'light': 5, 'dark': 6,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '062f219e852404144cd7967bcbac5d5d82c151697d8eacfd8c29779acbc58b19'}
            happyPath11 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
            happyPath12 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                      0, 0, 0, 0],
                            'integrity': '5df1fd1ccbd0dc74d65ab00d4d62f2e21c2def95dc47e7c73751986cdb5e8710'}
            happyPath13 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a'}
            happyPath14 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '66271cbb9037c515e73be3a74a37259a179f2d2861cf4e82130cd579a2141093'}
            happyPath15 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
            happyPath16 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                            'integrity': 'e2f7b8593ebadc126833074a7d8653d3c12c36ab3b7622a9cc6ac5dc1a0d9698'}
            happyPath17 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
                            'integrity': '7c53df9ff782bbbff544d876f4d69a1d87d5864295c0e4a6bf29e6a7ee5a96fc'}
            happyPath18 = {'light': 1, 'dark': 2, 'blank': 0,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
                                      1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': '8a1c0659575e8cdd01b2e4ff3f431c845e7e7960279bb7abfaa5465e4a755354'}
            
            # Happy path unit tests
            self.assertEqual(s._status(happyPath1), {'status': 'ok'})     # Happy path test 010: nominal light, nominal dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath2), {'status': 'ok'})     # Happy path test 020: high bound light, nominal dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath3), {'status': 'ok'})     # Happy path test 021: low bound light, nominal dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath4), {'status': 'ok'})     # Happy path test 022: missing light, nominal dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath5), {'status': 'ok'})     # Happy path test 030: nominal light, low bound dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath6), {'status': 'ok'})     # Happy path test 031: nominal light, high bound dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath7), {'status': 'ok'})     # Happy path test 032: nominal light, missing dark, nominal blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath8), {'status': 'ok'})     # Happy path test 040: nominal light, nominal dark, low bound blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath9), {'status': 'ok'})     # Happy path test 041: nominal light, nominal dark, high bound blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath10), {'status': 'ok'})    # Happy path test 042: nominal light, nominal dark, missing blank, nominal size, nominal board, nominal integrity
            self.assertEqual(s._status(happyPath11), {'status': 'ok'})    # Happy path test 050: nominal light, nominal dark, nominal blank, low bound size board with nominal elements, nominal integrity
            self.assertEqual(s._status(happyPath12), {'status': 'ok'})    # Happy path test 051: nominal light, nominal dark, nominal blank, high bound size board with nominal elements, nominal integrity
            self.assertEqual(s._status(happyPath13), {'status': 'ok'})    # Happy path test 060: nominal light, nominal dark, nominal blank, nominal board, dark next player
            self.assertEqual(s._status(happyPath14), {'status': 'ok'})    # Happy path test 061: nominal light, nominal dark, nominal blank, nominal board, light next player
            self.assertEqual(s._status(happyPath15), {'status': 'ok'})    # Happy path test 070: status is "ok"
            self.assertEqual(s._status(happyPath16), {'status': 'dark'})  # Happy path test 071: status is "dark"
            self.assertEqual(s._status(happyPath17), {'status': 'light'}) # Happy path test 072: status is "light"
            self.assertEqual(s._status(happyPath18), {'status': 'end'})   # Happy path test 073: status is "end"
            pass
    
        def testSadPaths(self):
            # Sad path data to be tested
            sadPath1 = {'light': 10, 'dark': 2, 'blank': 0,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 2, 1, 1, 1, 1, 2, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': 'b71bf3bee30fb8c3caa49752bcf9656870cfbd3bec4e4353e1e491054bf11c2f'}
            sadPath2 = {'light': -1, 'dark': 2, 'blank': 0,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 2, 1, 1, 1, 1, 2, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': 'f31631fdc7ba5ecd3096a306dbc7e43a9bc13fa781b91d83c36057f5050a51da'}
            sadPath3 = {'light': 'X', 'dark': 2, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'X', 2, 1, 1, 1, 1, 2, 'X', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': '8959fc376b23af1520014ef3bef1eb4f924ec692bbbcd9f638245bf85fb0a6da'}
            sadPath4 = {'light': None, 'dark': 2, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': '1cc0050055aa122edbb536cc63dfe515e6a55132a42a6c8fa41349ab6e572c6a'}
            sadPath5 = {'light': 5, 'dark': 10, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 10, 1, 1, 1, 1, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': 'e8a244c301df58429d82070942fe05dff389162c0aeec8383e3c82863ae09c62'}
            sadPath6 = {'light': 5, 'dark': -1, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, -1, 1, 1, 1, 1, -1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': '301e0f00c1b83b65adc1d4fd5e87aaf7f594aa20842ab1df86a6be2e144367db'}
            sadPath7 = {'light': 5, 'dark': 1.2, 'blank': 3,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1.2, 1, 1, 1, 1, 1.2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': 'e62a2ec6eb082391a6a5664b4f4dbd8130e43d6589267b19b831423bfcde4a9d'}
            sadPath8 = {'light': 5, 'dark': None, 'blank': 0,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '5d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'}
            sadPath9 = {'light': 1, 'dark': 2, 'blank': 10,
                            'board': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 10, 10, 10, 10, 2, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                            'integrity': '530242aec98aa07d3c025b9101bd5b840527cd9b03302641da18c801d70c37e8'}
            sadPath10 = {'light': 1, 'dark': 2, 'blank': -1,
                            'board': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 2, -1, -1, -1, -1, 2, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                            'integrity': '2e226315d3fc18cf5771b45ae78bfe7be9510ee98b6e566e382f8a70861c8e7d'}
            sadPath11 = {'light': 1, 'dark': 2, 'blank': '1E5',
                            'board': ['1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', 1, 2, '1E5', '1E5', '1E5', '1E5', 2, 1, '1E5',
                                      '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5', '1E5'],
                            'integrity': 'fe62b7f99befb02e21c50cc755a68ef80fb59d56224b02a1f2888e0830454773'}
            sadPath12 = {'light': 1, 'dark': 2, 'blank': None,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': '6c3ec0129f5e128f48e2541bd6663a52a825c35f99b9a69d9593f2fc44b0bb4b'}
            sadPath13 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '9d43a04297202bccc81a13b6857179269c0fe33e5227c6569286d54d82493ba6'}
            sadPath14 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'}
            sadPath15 = {'light': 1, 'dark': 2, 'blank': 0,
                            'integrity': '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'}
            sadPath16 = {'light': 1, 'dark': 2, 'blank': 0, 'board': None,
                            'integrity': '1e3f8bb2d56c5b4483c9f3dccf7bc16d339534a98020e9a28383aaa219f3e64d'}
            sadPath17 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465'}
            sadPath18 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465a00'}
            sadPath19 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'f01977c17f801c43eeb13fb9f74a49bd0c761db3cdffe01510f47ddd23ab465$'}
            sadPath20 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]}
            sadPath21 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': None}
            sadPath22 = {'light': 2, 'dark': 2, 'blank': 0,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': 'e50f93033edd2b27fd1c54631a4b574e545df9e8c06e0b4f74ca94841a4ab6c4'}
            sadPath23 = {'light': 1, 'dark': 2, 'blank': 1,
                            'board': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            'integrity': 'c725061d80e342070c231d2b987c476f92b8f3d9e5826c2223cff281562e8e2c'}
            sadPath24 = {'light': 1, 'dark': 2, 'blank': 2,
                            'board': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                            'integrity': '4edfe0aad5d491d98b8103e4f8f899cd3cef690f6ec3602a16e5a0e0301e8bd6'}
            sadPath25 = {'light': 9, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': 'b42a70b9f5b1064d1a1c594f466ec6cb1c2383694a8fe9f660d7fb07bcdce637'}
            sadPath26 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                            'integrity': '4d5aeb4a45b57eecf69dcc304664fcf7a6f7c74c86ef9ede14da46ab2d9df242'}
            sadPath27 = {'light': 1, 'dark': 2, 'blank': 3,
                            'board': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'integrity': 'c9fd7c0049f79f33e45998064cd1fca01600dd5cdc55cb3bf33169cd07c1905a'}
            
            # Sad path unit tests
            self.assertEqual(s._status(sadPath1), {'status': 'error: one of the parameters is out of the specified bounds'})  # Sad path test 900: above bound light, nominal dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath2), {'status': 'error: one of the parameters is out of the specified bounds'})  # Sad path test 901: below bound light, nominal dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath3), {'status': 'error: one of the parameters is not the correct type'})  # Sad path test 902: non-integer light, nominal dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath4), {'status': 'error: one of the parameters was passed a null value'})  # Sad path test 903: null light, nominal dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath5), {'status': 'error: one of the parameters is out of the specified bounds'})  # Sad path test 910: nominal light, above bound dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath6), {'status': 'error: one of the parameters is out of the specified bounds'})  # Sad path test 911: nominal light, below bound dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath7), {'status': 'error: one of the parameters is not the correct type'})  # Sad path test 912: nominal light, non-integer dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath8), {'status': 'error: one of the parameters was passed a null value'})  # Sad path test 913: nominal light, null dark, nominal blank, nominal size
            self.assertEqual(s._status(sadPath9), {'status': 'error: one of the parameters is out of the specified bounds'})  # Sad path test 920: nominal light, nominal dark, above bound blank, nominal size
            self.assertEqual(s._status(sadPath10), {'status': 'error: one of the parameters is out of the specified bounds'}) # Sad path test 921: nominal light, nominal dark, below bound blank, nominal size
            self.assertEqual(s._status(sadPath11), {'status': 'error: one of the parameters is not the correct type'}) # Sad path test 922: nominal light, nominal dark, non-integer blank, nominal size
            self.assertEqual(s._status(sadPath12), {'status': 'error: one of the parameters was passed a null value'}) # Sad path test 923: nominal light, nominal dark, null blank, nominal size
            self.assertEqual(s._status(sadPath13), {'status': 'error: the board size is not valid or was missing'}) # Sad path test 930: nominal light, nominal dark, nominal blank, non-square board, nominal integrity
            self.assertEqual(s._status(sadPath14), {'status': 'error: the board size is not valid or was missing'}) # Sad path test 931: nominal light, nominal dark, nominal blank, odd x odd board, nominal integrity
            self.assertEqual(s._status(sadPath15), {'status': 'error: the board size is not valid or was missing'}) # Sad path test 932: nominal light, nominal dark, nominal blank, missing board, nominal integrity
            self.assertEqual(s._status(sadPath16), {'status': 'error: one of the parameters was passed a null value'}) # Sad path test 933: nominal light, nominal dark, nominal blank, null board, nominal integrity
            self.assertEqual(s._status(sadPath17), {'status': 'error: the integrity hash is incorrect or missing'}) # Sad path test 940: nominal light, nominal dark, nominal blank, nominal board, short integrity
            self.assertEqual(s._status(sadPath18), {'status': 'error: the integrity hash is incorrect or missing'}) # Sad path test 941: nominal light, nominal dark, nominal blank, nominal board, long integrity
            self.assertEqual(s._status(sadPath19), {'status': 'error: the integrity hash is incorrect or missing'}) # Sad path test 942: nominal light, nominal dark, nominal blank, nominal board, non-hex integrity
            self.assertEqual(s._status(sadPath20), {'status': 'error: the integrity hash is incorrect or missing'}) # Sad path test 943: nominal light, nominal dark, nominal blank, nominal board, missing integrity
            self.assertEqual(s._status(sadPath21), {'status': 'error: one of the parameters was passed a null value'}) # Sad path test 944: nominal light, nominal dark, nominal blank, nominal board, null integrity
            self.assertEqual(s._status(sadPath22), {'status': 'error: the light, dark and blank parameters have a value in common'}) # Sad path test 950: nominal light, dark = light, nominal blank, nominal board, nominal integrity
            self.assertEqual(s._status(sadPath23), {'status': 'error: the light, dark and blank parameters have a value in common'}) # Sad path test 951: nominal light, nominal dark, blank = light, nominal board, nominal integrity
            self.assertEqual(s._status(sadPath24), {'status': 'error: the light, dark and blank parameters have a value in common'}) # Sad path test 952: nominal light, nominal dark, blank = dark, nominal board, nominal integrity
            self.assertEqual(s._status(sadPath25), {'status': 'error: the token values provided do not match the tokens listed in the board'}) # Sad path test 953: nominal light, nominal dark, nominal blank, board with non-light/dark/blank values, nominal integrity
            self.assertEqual(s._status(sadPath26), {'status': 'error: the integrity hash is incorrect or missing'}) # Sad path test 954: nominal light, nominal dark, nominal blank, nominal board, invalid integrity
            self.assertEqual(s._status(sadPath27), {'status': 'error: the token values provided do not match the tokens listed in the board'}) # Sad path test 955: nominal light, nominal dark, nominal blank, board with non-light/dark/blank tokens, nominal integrity
            pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()