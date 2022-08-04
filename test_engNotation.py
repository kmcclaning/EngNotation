"""
Test engNotation.py engineering notation number pretty-printer
"""

__author__ = "K.J. McClaning"
__created__ = "2022-07-26"
__updated__ = "2022-08-04"
__version__ = "0.0.2"

#  MIT License
#
#  Copyright (c) 2022 K.J.McClaning
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import math
from unittest import TestCase

from engNotation import EngNotation

testL = [
    {'val': 0, 'unitS': '', 'precision': 0, 'resultS': '0.00'},
    {'val': 0, 'unitS': 'erg^3', 'precision': 2, 'resultS': '0.0000 erg^3'},
    {'val': -0, 'unitS': '', 'precision': 0, 'resultS': '0.00'},
    {'val': -0, 'unitS': 'erg^3', 'precision': 2, 'resultS': '0.0000 erg^3'},

    {'val': math.nan, 'unitS': '', 'precision': 0, 'resultS': 'NAN'},
    {'val': math.nan, 'unitS': 'erg^2', 'precision': 2, 'resultS': 'NAN erg^2'},
    {'val': math.inf, 'unitS': '', 'precision': 0, 'resultS': 'INF'},
    {'val': -math.inf, 'unitS': 'HP', 'precision': 1, 'resultS': '-INF HP'},
    {'val': 1000000, 'unitS': '', 'precision': 0, 'resultS': '1.00M'},
    {'val': 100000, 'unitS': '', 'precision': 0, 'resultS': '100k'},
    {'val': 10000, 'unitS': '', 'precision': 0, 'resultS': '10.0k'},
    {'val': 1000, 'unitS': '', 'precision': 0, 'resultS': '1.00k'},
    {'val': 100, 'unitS': '', 'precision': 0, 'resultS': '100'},
    {'val': 10, 'unitS': '', 'precision': 0, 'resultS': '10.0'},
    {'val': 1, 'unitS': '', 'precision': 0, 'resultS': '1.00'},

    {'val': -1000000, 'unitS': '', 'precision': 0, 'resultS': '-1.00M'},
    {'val': -100000, 'unitS': '', 'precision': 0, 'resultS': '-100k'},
    {'val': -10000, 'unitS': '', 'precision': 0, 'resultS': '-10.0k'},
    {'val': -1000, 'unitS': '', 'precision': 0, 'resultS': '-1.00k'},
    {'val': -100, 'unitS': '', 'precision': 0, 'resultS': '-100'},
    {'val': -10, 'unitS': '', 'precision': 0, 'resultS': '-10.0'},
    {'val': -1, 'unitS': '', 'precision': 0, 'resultS': '-1.00'},

    {'val': 2.718281828e-26, 'unitS': '', 'precision': 0, 'resultS': '27.2e-27'},
    {'val': 2.718281828e-25, 'unitS': '', 'precision': 0, 'resultS': '272e-27'},
    {'val': 2.718281828e-24, 'unitS': '', 'precision': 0, 'resultS': '2.72e-24'},
    {'val': 2.718281828e-23, 'unitS': '', 'precision': 0, 'resultS': '27.2e-24'},
    {'val': 2.718281828e-22, 'unitS': '', 'precision': 0, 'resultS': '272e-24'},
    {'val': 2.718281828e-21, 'unitS': '', 'precision': 0, 'resultS': '2.72e-21'},
    {'val': 2.718281828e-20, 'unitS': '', 'precision': 0, 'resultS': '27.2e-21'},
    {'val': 2.718281828e-19, 'unitS': '', 'precision': 0, 'resultS': '272e-21'},
    {'val': 2.718281828e-18, 'unitS': '', 'precision': 0, 'resultS': '2.72a'},
    {'val': 2.718281828e-17, 'unitS': '', 'precision': 0, 'resultS': '27.2a'},
    {'val': 2.718281828e-16, 'unitS': '', 'precision': 0, 'resultS': '272a'},
    {'val': 2.718281828e-15, 'unitS': '', 'precision': 0, 'resultS': '2.72f'},
    {'val': 2.718281828e-14, 'unitS': '', 'precision': 0, 'resultS': '27.2f'},
    {'val': 2.718281828e-13, 'unitS': '', 'precision': 0, 'resultS': '272f'},
    {'val': 2.718281828e-12, 'unitS': '', 'precision': 0, 'resultS': '2.72p'},
    {'val': 2.718281828e-11, 'unitS': '', 'precision': 0, 'resultS': '27.2p'},
    {'val': 2.718281828e-10, 'unitS': '', 'precision': 0, 'resultS': '272p'},
    {'val': 2.718281828e-09, 'unitS': '', 'precision': 0, 'resultS': '2.72n'},
    {'val': 2.718281828e-08, 'unitS': '', 'precision': 0, 'resultS': '27.2n'},
    {'val': 2.718281828e-07, 'unitS': '', 'precision': 0, 'resultS': '272n'},
    {'val': 2.718281828e-06, 'unitS': '', 'precision': 0, 'resultS': '2.72u'},
    {'val': 2.718281828e-05, 'unitS': '', 'precision': 0, 'resultS': '27.2u'},
    {'val': 0.0002718281828, 'unitS': '', 'precision': 0, 'resultS': '272u'},
    {'val': 0.002718281828, 'unitS': '', 'precision': 0, 'resultS': '2.72m'},
    {'val': 0.02718281828, 'unitS': '', 'precision': 0, 'resultS': '27.2m'},
    {'val': 0.2718281828, 'unitS': '', 'precision': 0, 'resultS': '272m'},
    {'val': 2.718281828, 'unitS': '', 'precision': 0, 'resultS': '2.72'},
    {'val': 27.18281828, 'unitS': '', 'precision': 0, 'resultS': '27.2'},
    {'val': 271.8281828, 'unitS': '', 'precision': 0, 'resultS': '272'},
    {'val': 2718.281828, 'unitS': '', 'precision': 0, 'resultS': '2.72k'},
    {'val': 27182.81828, 'unitS': '', 'precision': 0, 'resultS': '27.2k'},
    {'val': 271828.1828, 'unitS': '', 'precision': 0, 'resultS': '272k'},
    {'val': 2718281.828, 'unitS': '', 'precision': 0, 'resultS': '2.72M'},
    {'val': 27182818.28, 'unitS': '', 'precision': 0, 'resultS': '27.2M'},
    {'val': 271828182.8, 'unitS': '', 'precision': 0, 'resultS': '272M'},
    {'val': 2718281828.0, 'unitS': '', 'precision': 0, 'resultS': '2.72G'},
    {'val': 27182818280.0, 'unitS': '', 'precision': 0, 'resultS': '27.2G'},
    {'val': 271828182799.99997, 'unitS': '', 'precision': 0, 'resultS': '272G'},
    {'val': 2718281828000.0, 'unitS': '', 'precision': 0, 'resultS': '2.72T'},
    {'val': 27182818280000.0, 'unitS': '', 'precision': 0, 'resultS': '27.2T'},
    {'val': 271828182800000.0, 'unitS': '', 'precision': 0, 'resultS': '272T'},
    {'val': 2718281828000000.0, 'unitS': '', 'precision': 0, 'resultS': '2.72P'},
    {'val': 2.718281828e+16, 'unitS': '', 'precision': 0, 'resultS': '27.2P'},
    {'val': 2.718281828e+17, 'unitS': '', 'precision': 0, 'resultS': '272P'},
    {'val': 2.718281828e+19, 'unitS': '', 'precision': 0, 'resultS': '27.2E'},
    {'val': 2.718281828e+20, 'unitS': '', 'precision': 0, 'resultS': '272E'},
    {'val': 2.718281828e+21, 'unitS': '', 'precision': 0, 'resultS': '2.72e21'},
    {'val': 2.718281828e+22, 'unitS': '', 'precision': 0, 'resultS': '27.2e21'},
    {'val': 2.718281828e+23, 'unitS': '', 'precision': 0, 'resultS': '272e21'},
    {'val': 2.718281828e+24, 'unitS': '', 'precision': 0, 'resultS': '2.72e24'},
    {'val': 2.718281823e+25, 'unitS': '', 'precision': 0, 'resultS': '27.2e24'},

    {'val': 1.234568e-26, 'unitS': 'A', 'precision': 0, 'resultS': "12.3e-27 A"},
    {'val': 1.234568e-25, 'unitS': 'A', 'precision': 0, 'resultS': "123e-27 A"},
    {'val': 1.234568e-24, 'unitS': 'A', 'precision': 0, 'resultS': "1.23e-24 A"},
    {'val': 1.234568e-23, 'unitS': 'A', 'precision': 0, 'resultS': "12.3e-24 A"},
    {'val': 1.234568e-22, 'unitS': 'A', 'precision': 0, 'resultS': "123e-24 A"},
    {'val': 1.234568e-21, 'unitS': 'A', 'precision': 0, 'resultS': "1.23e-21 A"},
    {'val': 1.234568e-20, 'unitS': 'A', 'precision': 0, 'resultS': "12.3e-21 A"},
    {'val': 1.234568e-19, 'unitS': 'A', 'precision': 0, 'resultS': "123e-21 A"},
    {'val': 1.234568e-18, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 aA"},
    {'val': 1.234568e-17, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 aA"},
    {'val': 1.234568e-16, 'unitS': 'A', 'precision': 0, 'resultS': "123 aA"},
    {'val': 1.234568e-15, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 fA"},
    {'val': 1.234568e-14, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 fA"},
    {'val': 1.234568e-13, 'unitS': 'A', 'precision': 0, 'resultS': "123 fA"},
    {'val': 1.234568e-12, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 pA"},
    {'val': 1.234568e-11, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 pA"},
    {'val': 1.234568e-10, 'unitS': 'A', 'precision': 0, 'resultS': "123 pA"},
    {'val': 1.234568e-09, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 nA"},
    {'val': 1.234568e-08, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 nA"},
    {'val': 1.234568e-07, 'unitS': 'A', 'precision': 0, 'resultS': "123 nA"},
    {'val': 1.234568e-06, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 uA"},
    {'val': 1.234568e-05, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 uA"},
    {'val': 1.234568e-04, 'unitS': 'A', 'precision': 0, 'resultS': "123 uA"},
    {'val': 1.234568e-03, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 mA"},
    {'val': 1.234568e-02, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 mA"},
    {'val': 1.234568e-01, 'unitS': 'A', 'precision': 0, 'resultS': "123 mA"},
    {'val': 1.234568e+00, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 A"},
    {'val': 1.234568e+01, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 A"},
    {'val': 1.234568e+02, 'unitS': 'A', 'precision': 0, 'resultS': "123 A"},
    {'val': 1.234568e+03, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 kA"},
    {'val': 1.234568e+04, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 kA"},
    {'val': 1.234568e+05, 'unitS': 'A', 'precision': 0, 'resultS': "123 kA"},
    {'val': 1.234568e+06, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 MA"},
    {'val': 1.234568e+07, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 MA"},
    {'val': 1.234568e+08, 'unitS': 'A', 'precision': 0, 'resultS': "123 MA"},
    {'val': 1.234568e+09, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 GA"},
    {'val': 1.234568e+10, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 GA"},
    {'val': 1.234568e+11, 'unitS': 'A', 'precision': 0, 'resultS': "123 GA"},
    {'val': 1.234568e+12, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 TA"},
    {'val': 1.234568e+13, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 TA"},
    {'val': 1.234568e+14, 'unitS': 'A', 'precision': 0, 'resultS': "123 TA"},
    {'val': 1.234568e+15, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 PA"},
    {'val': 1.234568e+16, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 PA"},
    {'val': 1.234568e+17, 'unitS': 'A', 'precision': 0, 'resultS': "123 PA"},
    {'val': 1.234568e+18, 'unitS': 'A', 'precision': 0, 'resultS': "1.23 EA"},
    {'val': 1.234568e+19, 'unitS': 'A', 'precision': 0, 'resultS': "12.3 EA"},
    {'val': 1.234568e+20, 'unitS': 'A', 'precision': 0, 'resultS': "123 EA"},
    {'val': 1.234568e+21, 'unitS': 'A', 'precision': 0, 'resultS': "1.23e21 A"},
    {'val': 1.234568e+22, 'unitS': 'A', 'precision': 0, 'resultS': "12.3e21 A"},
    {'val': 1.234568e+23, 'unitS': 'A', 'precision': 0, 'resultS': "123e21 A"},
    {'val': 1.234568e+24, 'unitS': 'A', 'precision': 0, 'resultS': "1.23e24 A"},
    {'val': 1.234568e+25, 'unitS': 'A', 'precision': 0, 'resultS': "12.3e24 A"},

    {'val': 9.87654321e-26, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77e-27 Ohm'},
    {'val': 9.87654321e-25, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7e-27 Ohm'},
    {'val': 9.87654321e-24, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877e-24 Ohm'},
    {'val': 9.87654321e-23, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77e-24 Ohm'},
    {'val': 9.87654321e-22, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7e-24 Ohm'},
    {'val': 9.87654321e-21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877e-21 Ohm'},
    {'val': 9.87654321e-20, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77e-21 Ohm'},
    {'val': 9.87654321e-19, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7e-21 Ohm'},
    {'val': 9.87654321e-18, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 aOhm'},
    {'val': 9.87654321e-17, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 aOhm'},
    {'val': 9.87654321e-16, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 aOhm'},
    {'val': 9.87654321e-15, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 fOhm'},
    {'val': 9.87654321e-14, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 fOhm'},
    {'val': 9.87654321e-13, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 fOhm'},
    {'val': 9.87654321e-12, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 pOhm'},
    {'val': 9.87654321e-11, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 pOhm'},
    {'val': 9.87654321e-10, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 pOhm'},
    {'val': 9.87654321e-09, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 nOhm'},
    {'val': 9.87654321e-08, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 nOhm'},
    {'val': 9.87654321e-07, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 nOhm'},
    {'val': 9.876543218e-06, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 uOhm'},
    {'val': 9.87654321e-05, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 uOhm'},
    {'val': 0.000987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 uOhm'},
    {'val': 0.00987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 mOhm'},
    {'val': 0.0987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 mOhm'},
    {'val': 0.987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 mOhm'},
    {'val': 9.87654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 Ohm'},
    {'val': 98.7654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 Ohm'},
    {'val': 987.654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 Ohm'},
    {'val': 9876.54321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 kOhm'},
    {'val': 98765.4321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 kOhm'},
    {'val': 987654.321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 kOhm'},
    {'val': 9876543.21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 MOhm'},
    {'val': 98765432.1, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 MOhm'},
    {'val': 987654321.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 MOhm'},
    {'val': 9876543210.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 GOhm'},
    {'val': 98765432100.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 GOhm'},
    {'val': 987654321000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 GOhm'},
    {'val': 9876543210000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 TOhm'},
    {'val': 98765432100000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 TOhm'},
    {'val': 987654321000000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 TOhm'},
    {'val': 9876543210000000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 POhm'},
    {'val': 9.87654321e+16, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 POhm'},
    {'val': 9.87654321e+17, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 POhm'},
    {'val': 9.87654321e+18, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877 EOhm'},
    {'val': 9.87654321e+19, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77 EOhm'},
    {'val': 9.87654321e+20, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7 EOhm'},
    {'val': 9.87654321e+21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877e21 Ohm'},
    {'val': 9.87654321e+22, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77e21 Ohm'},
    {'val': 9.87654321e+23, 'unitS': 'Ohm', 'precision': 1, 'resultS': '987.7e21 Ohm'},
    {'val': 9.87654321e+24, 'unitS': 'Ohm', 'precision': 1, 'resultS': '9.877e24 Ohm'},
    {'val': 9.87654321e+25, 'unitS': 'Ohm', 'precision': 1, 'resultS': '98.77e24 Ohm'},

    {'val': -9.87654321e-26, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77e-27 Ohm'},
    {'val': -9.87654321e-25, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7e-27 Ohm'},
    {'val': -9.87654321e-24, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877e-24 Ohm'},
    {'val': -9.87654321e-23, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77e-24 Ohm'},
    {'val': -9.87654321e-22, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7e-24 Ohm'},
    {'val': -9.87654321e-21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877e-21 Ohm'},
    {'val': -9.87654321e-20, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77e-21 Ohm'},
    {'val': -9.87654321e-19, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7e-21 Ohm'},
    {'val': -9.87654321e-18, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 aOhm'},
    {'val': -9.87654321e-17, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 aOhm'},
    {'val': -9.87654321e-16, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 aOhm'},
    {'val': -9.87654321e-15, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 fOhm'},
    {'val': -9.87654321e-14, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 fOhm'},
    {'val': -9.87654321e-13, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 fOhm'},
    {'val': -9.87654321e-12, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 pOhm'},
    {'val': -9.87654321e-11, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 pOhm'},
    {'val': -9.87654321e-10, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 pOhm'},
    {'val': -9.87654321e-09, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 nOhm'},
    {'val': -9.87654321e-08, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 nOhm'},
    {'val': -9.87654321e-07, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 nOhm'},
    {'val': -9.876543218e-06, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 uOhm'},
    {'val': -9.87654321e-05, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 uOhm'},
    {'val': -0.000987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 uOhm'},
    {'val': -0.00987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 mOhm'},
    {'val': -0.0987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 mOhm'},
    {'val': -0.987654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 mOhm'},
    {'val': -9.87654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 Ohm'},
    {'val': -98.7654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 Ohm'},
    {'val': -987.654321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 Ohm'},
    {'val': -9876.54321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 kOhm'},
    {'val': -98765.4321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 kOhm'},
    {'val': -987654.321, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 kOhm'},
    {'val': -9876543.21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 MOhm'},
    {'val': -98765432.1, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 MOhm'},
    {'val': -987654321.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 MOhm'},
    {'val': -9876543210.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 GOhm'},
    {'val': -98765432100.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 GOhm'},
    {'val': -987654321000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 GOhm'},
    {'val': -9876543210000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 TOhm'},
    {'val': -98765432100000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 TOhm'},
    {'val': -987654321000000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 TOhm'},
    {'val': -9876543210000000.0, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 POhm'},
    {'val': -9.87654321e+16, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 POhm'},
    {'val': -9.87654321e+17, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 POhm'},
    {'val': -9.87654321e+18, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877 EOhm'},
    {'val': -9.87654321e+19, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77 EOhm'},
    {'val': -9.87654321e+20, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7 EOhm'},
    {'val': -9.87654321e+21, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877e21 Ohm'},
    {'val': -9.87654321e+22, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77e21 Ohm'},
    {'val': -9.87654321e+23, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-987.7e21 Ohm'},
    {'val': -9.87654321e+24, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-9.877e24 Ohm'},
    {'val': -9.87654321e+25, 'unitS': 'Ohm', 'precision': 1, 'resultS': '-98.77e24 Ohm'},

    {'val': 1e-26, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000e-27 V'},
    {'val': 1e-23, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000e-24 V'},
    {'val': 1e-20, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000e-21 V'},
    {'val': 1e-17, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 aV'},
    {'val': 1e-14, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 fV'},
    {'val': 1e-11, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 pV'},
    {'val': 1e-08, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 nV'},
    {'val': 1e-05, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 uV'},
    {'val': 0.01, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 mV'},
    {'val': 10.0, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 V'},
    {'val': 10000.0, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 kV'},
    {'val': 10000000.0, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 MV'},
    {'val': 10000000000.0, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 GV'},
    {'val': 10000000000000.0, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 TV'},
    {'val': 1e+16, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 PV'},
    {'val': 1e+19, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000 EV'},
    {'val': 1e+22, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000e21 V'},
    {'val': 1e+25, 'unitS': 'V', 'precision': 4, 'resultS': '10.00000e24 V'},

    {'val': 4.2e-25, 'unitS': 'J', 'precision': 8, 'resultS': '420.00000000e-27 J'},
    {'val': 4.2e-20, 'unitS': 'J', 'precision': 8, 'resultS': '42.000000000e-21 J'},
    {'val': 4.2e-15, 'unitS': 'J', 'precision': 8, 'resultS': '4.2000000000 fJ'},
    {'val': 4.2e-10, 'unitS': 'J', 'precision': 8, 'resultS': '420.00000000 pJ'},
    {'val': 4.2e-05, 'unitS': 'J', 'precision': 8, 'resultS': '42.000000000 uJ'},
    {'val': 4.2, 'unitS': 'J', 'precision': 8, 'resultS': '4.2000000000 J'},
    {'val': 420000.0, 'unitS': 'J', 'precision': 8, 'resultS': '420.00000000 kJ'},
    {'val': 42000000000.0, 'unitS': 'J', 'precision': 8, 'resultS': '42.000000000 GJ'},
    {'val': 4200000000000000.0, 'unitS': 'J', 'precision': 8, 'resultS': '4.2000000000 PJ'},
    {'val': 4.2e+20, 'unitS': 'J', 'precision': 8, 'resultS': '420.00000000 EJ'},
    {'val': 4.2e+25, 'unitS': 'J', 'precision': 8, 'resultS': '42.000000000e24 J'},

    {'val': -4.2e-25, 'unitS': 'J', 'precision': 8, 'resultS': '-420.00000000e-27 J'},
    {'val': -4.2e-20, 'unitS': 'J', 'precision': 8, 'resultS': '-42.000000000e-21 J'},
    {'val': -4.2e-15, 'unitS': 'J', 'precision': 8, 'resultS': '-4.2000000000 fJ'},
    {'val': -4.2e-10, 'unitS': 'J', 'precision': 8, 'resultS': '-420.00000000 pJ'},
    {'val': -4.2e-05, 'unitS': 'J', 'precision': 8, 'resultS': '-42.000000000 uJ'},
    {'val': -4.2, 'unitS': 'J', 'precision': 8, 'resultS': '-4.2000000000 J'},
    {'val': -420000.0, 'unitS': 'J', 'precision': 8, 'resultS': '-420.00000000 kJ'},
    {'val': -42000000000.0, 'unitS': 'J', 'precision': 8, 'resultS': '-42.000000000 GJ'},
    {'val': -4200000000000000.0, 'unitS': 'J', 'precision': 8, 'resultS': '-4.2000000000 PJ'},
    {'val': -4.2e+20, 'unitS': 'J', 'precision': 8, 'resultS': '-420.00000000 EJ'},
    {'val': -4.2e+25, 'unitS': 'J', 'precision': 8, 'resultS': '-42.000000000e24 J'},

]


class TestEngNotation(TestCase):

    def test_eng_notation(self):
        """
        test the engineering notation routines
        :return boolean: assertion results
        """
        testCount = 1
        for thisTestD in testL:
            eN = EngNotation(
                thisTestD['val'],
                precision=thisTestD['precision'],
                unitS=thisTestD['unitS'],
            )
            s = '%s' % eN
            print('%i: ' % testCount + s)
            testCount += 1
            self.assertEqual(s, thisTestD['resultS'])

        # used to generate the known good dictionaries in testL when EngNotation is
        # in a known good state

        # # integers, NaNs, infinite and other weirdness
        # # zero
        # thisVal = 0
        # eN = EngNotation(thisVal)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '', 'precision': 0, 'resultS': '{1}'}},".format(thisVal,eN)
        # print(s)
        #
        # thisVal = 0
        # unitS = 'erg'
        # precision = 2
        # eN = EngNotation(thisVal,unitS = unitS)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisVal,precision,unitS,eN)
        # print(s)
        #
        # # nan
        # thisVal = math.nan
        # eN = EngNotation(thisVal)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '', 'precision': 0, 'resultS': '{1}'}},".format(thisVal,eN)
        # print(s)
        #
        # thisVal = math.nan
        # unitS = 'erg'
        # precision = 2
        # eN = EngNotation(thisVal,unitS = unitS)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisVal,precision,unitS,eN)
        # print(s)
        #
        # thisVal = math.inf
        # eN = EngNotation(thisVal)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '', 'precision': 0, 'resultS': '{1}'}},".format(thisVal,eN)
        # print(s)
        #
        # thisVal = -math.inf
        # unitS = 'HP'
        # precision = 1
        # eN = EngNotation(thisVal,unitS = unitS)
        # s = '%6e: %s' % (thisVal, eN)
        # s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisVal,precision,unitS,eN)
        # print(s)
        #
        # # integers
        # mantissa = 1000000
        # unitS = ''
        # precision = 0
        # while mantissa > 0:
        #     eN = EngNotation(mantissa, precision=precision, unitS=unitS)
        #     s = '%6e: %s' % (mantissa, eN)
        #     s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(mantissa, unitS, precision, eN)
        #     print(s)
        #     mantissa = mantissa // 10

        # mantissa = 2.718281828
        # unitS = ''
        # precision = 0
        # thisExp = -26
        # while thisExp < 26:
        #     thisNum = mantissa * 10 ** thisExp
        #     eN = EngNotation(thisNum, precision=precision, unitS=unitS)
        #     s = '%6e: %s' % (thisNum, eN)
        #     s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisNum, unitS, precision, eN)
        #     print(s)
        #     thisExp += 1

        # mantissa = 1.23456789
        # thisExp = -26
        # while thisExp < 26:
        #     thisNum = mantissa * 10**thisExp
        #     eN = EngNotation(thisNum, unitS='A')
        #     s = '%6e: %s' % (thisNum,eN)
        #     print(s)
        #     thisExp += 1

        # mantissa = 9.87654321
        # unitS = 'Ohm'
        # precision = 1
        # thisExp = -26
        # while thisExp < 26:
        #     thisNum = mantissa * 10 ** thisExp
        #     eN = EngNotation(thisNum, precision=precision, unitS=unitS)
        #     s = '%6e: %s' % (thisNum, eN)
        #     s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisNum, unitS, precision, eN)
        #     print(s)
        #     thisExp += 1

        # mantissa = 1.0
        # unitS = 'V'
        # precision = 4
        # thisExp = -26
        # while thisExp < 26:
        #     thisNum = mantissa * 10 ** thisExp
        #     eN = EngNotation(thisNum, precision=precision, unitS=unitS)
        #     s = '%6e: %s' % (thisNum, eN)
        #     s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisNum, unitS, precision, eN)
        #     print(s)
        #     thisExp += 3

        # mantissa = 42.0
        # unitS = 'J'
        # precision = 8
        # thisExp = -26
        # while thisExp < 26:
        #     thisNum = mantissa * 10 ** thisExp
        #     eN = EngNotation(thisNum, precision=precision, unitS=unitS)
        #     s = '%6e: %s' % (thisNum, eN)
        #     s = "    {{'val': {0}, 'unitS': '{1}', 'precision': {2}, 'resultS': '{3}'}},".format(thisNum, unitS, precision, eN)
        #     print(s)
        #     thisExp += 5

# ===========================================================================
