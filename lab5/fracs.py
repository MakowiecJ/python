def add_frac(frac1, frac2):        # frac1 + frac2
    if frac1[1] == frac2[1]: return [frac1[0] + frac2[0], frac1[1]]
    else: return [frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]]

def sub_frac(frac1, frac2):        # frac1 - frac2
    if frac1[1] == frac2[1]: return [frac1[0] - frac2[0], frac1[1]]
    else: return [frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]]

def mul_frac(frac1, frac2):        # frac1 * frac2
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):       # frac1 / frac2
    return mul_frac(frac1, [frac2[1], frac2[0]])

def is_positive(frac):             # bool, czy dodatni
    if frac[0] >= 0 and frac[1] > 0: return True
    elif frac[0] <

def is_zero(frac): pass                 # bool, typu [0, x]

def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1

def frac2float(frac): pass              # konwersja do float


# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([3, 2], [2, 3]), [5, 6])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([2, 3], [1, 2]), [2, 6])

    def test_div_frac(self): 
        self.assertEqual(div_frac([4, 2], [2, 1]), [4, 4])

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

