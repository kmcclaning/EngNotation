# -*- coding: utf-8 -*-
"""
Pretty-prints values in engineer-friendly formats e.g. 0.003 is printed
as "3.00m". If a unit is passed (e.g. "Ohm"), then the quantity is
printed as "3.00 mOhm". Based upon:
https://github.com/slightlynybbled/engineering_notation
and the HP35 calculator documentation. From the HP-35 calculator documentation:
ENG format displays a number in a manner similar to scientific notation, except that
the exponent is a multiple of three (there can be up to three digits before the "."
radix mark). This format is most useful for scientific and engineering calculations
that use units specified in multiples of 10^3 (such as micro–, milli–, and kilo–units.)
For example, in the number 123.46e3, the "2", "3", "4", and "6" are the
significant digits after the first significant digit you see when the calculator is
set to ENG 4 display mode. The "3" following the "e" is the (multiple of 3)
exponent of 10: 123.46 x 10^3
"""

__author__ = "K.J. McClaning"
__created__ = "2020-10-02"
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

_prefixD = {
    18: "E",  # Exa
    15: "P",  # Pera
    12: "T",  # Tera
    9: "G",  # Giga
    6: "M",  # Mega
    3: "k",  # kilo
    0: "",  # base unit
    -3: "m",  # milli
    -6: "u",  # micro
    -9: "n",  # nano
    -12: "p",  # pico
    -15: "f",  # femto
    -18: "a",  # atto
}


class EngNotation:
    """
    Allows the user to express and print a number in engineering notation, with an optional units string.
    The display format is meant to follow the behavior of the HP-25/HP-42 series of calculators.
    If a unit string is passed (e.g. "Ohm"), then the quantity is printed as "33.00 mOhm"
    """

    def __init__(self, value, precision=0, unitS='', ):
        """
        initializes a number to be expressed in engineering notation
        :rtype: object
        :param float,int value: value to be expressed
        :param int precision: number of digits to be expressed, beyond 3
        :param string unitS: optional unit string e.g. "Ohm" or "V"
        """
        self.value = value
        self.precision = precision
        self.unitS = unitS

        # handle the inf and nan cases in the __repr__ method
        if math.isnan(self.value) or math.isinf(self.value):
            return

        # retrieve the base-10 exponent and generate a mantissa between
        # 1.0 and 9.999...
        # the try/except handles the 0.0, nan, inf, etc cases
        try:
            self.exponent = int(math.log10(abs(self.value)))
            self.mantissa = self.value / 10 ** self.exponent
        except ValueError:
            self.exponent = 1
            self.mantissa = 0.0

        # adjust the mantissa and exponent for numbers less than 1.0
        if abs(self.mantissa) < 1.0:
            self.mantissa *= 10.0
            self.exponent -= 1

        # generate the engineering format version of the input value and its exponent
        exponentMod = self.exponent % 3
        exponent3 = self.exponent - exponentMod
        if exponentMod == 0:
            self.engExponent = self.exponent
            self.engValue = self.mantissa
        elif exponentMod == 1:
            self.engExponent = self.exponent - 1
            self.engValue = self.mantissa * 10.0
        else:  # exponentMod == 2:
            self.engExponent = self.exponent - 2
            self.engValue = self.mantissa * 100.0

        # find the unit prefix appropriate for the engineering notation exponent
        if exponent3 in _prefixD.keys():
            self.prefixS = _prefixD[exponent3]
            self.foundPrefix = True
        else:
            self.prefixS = "E%i" % self.engExponent
            self.foundPrefix = False

    def __repr__(self):
        """
        Returns the engineering formatted number as a string, optionally
        with the units attached, if present
        :return: a string representing the engineering number
        """

        # handle the inf and nan cases specially
        if math.isnan(self.value):
            s = 'NAN'
            if len(self.unitS) > 0:
                s += ' ' + self.unitS
            return s

        # true if inf or -inf
        if math.isinf(self.value):
            if self.value < 0:
                s = '-INF'
            else:
                s = 'INF'
            if len(self.unitS) > 0:
                s += ' ' + self.unitS
            return s

        # format the engineering notation mantissa to the required precision
        # the precision in the format string speaks to the number of decimal digits
        # beyond 3.
        numDigits = 3 + self.precision

        # format the return string based upon the number of digits req'd
        if abs(self.engValue) < 10.0:
            s = '{:.{}f}'.format(self.engValue, numDigits - 1)
        elif abs(self.engValue) < 100.0:
            s = '{:.{}f}'.format(self.engValue, numDigits - 2)
        else:
            s = '{:.{}f}'.format(self.engValue, numDigits - 3)

        # if we found a prefix in the table e.g. "k" or "u"
        if self.foundPrefix:

            # do we have a units string?
            if len(self.unitS) == 0:
                s += self.prefixS
            else:
                s += " " + self.prefixS + self.unitS

        # we didn't find a prefix in the table
        else:

            # do we have a units string?
            if len(self.unitS) == 0:
                s += "e%i" % self.engExponent
            else:
                s += "e%i " % self.engExponent + self.unitS

        return s

    def __str__(self):
        """
        Returns the string representation of the engineering number
        :return: a string representing the engineering number
        """
        return self.__repr__()

# ===========================================================================
