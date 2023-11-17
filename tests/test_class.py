from copy import copy
from my_class import Diag


class TestDiag:
    #To test: pytest  -s -vv
    def test_diag_str(self):
        a = Diag('abc')
        assert str(a) == 'a\n b\n  c'

    def test_second_case(self):
        obj1 = Diag("123") + Diag("456")
        assert obj1 == Diag("654321")

    def test_diag_sub(self):
        a, b = Diag("abcab"), Diag("ba")
        a_cp, b_cp = copy(a), copy(b)
        assert a - b == Diag("cab")
        assert a == a_cp
        assert b == b_cp

    def test_diag_mul(self):
        f = Diag('abc')
        g = Diag('3')
        assert f * g == Diag('abcabcabc')

    def test_diag_iter(self):
        h = Diag('abcdefghijklmnopqrstuvwxyz')
        assert list(h) == ['a', 'a', 'b', 'c', 'e', 'h', 'm', 'u']