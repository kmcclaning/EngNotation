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

__updated__ = "2022-01-23"
__version__ = "1.0.0"

import math

_prefixD = {18: "E",  # Exa
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

# For example,
#     value       precision   string result
#     0.033       0           "30.m"
#     0.033       1           "33.m"
#     0.033       2           "33.0m"
#     0.033       3           "33.00m"

#
#
# from decimal import Decimal
# from string import digits
#
# _suffix_lookup = {
#     'y': 'e-24',
#     'z': 'e-21',
#     'a': 'e-18',
#     'f': 'e-15',
#     'p': 'e-12',
#     'n': 'e-9',
#     'u': 'e-6',
#     'm': 'e-3',
#     '': 'e0',
#     'k': 'e3',
#     'M': 'e6',
#     'G': 'e9',
#     'T': 'e12'
# }
#
# _exponent_lookup_scaled = {
#     '-48': 'y',
#     '-45': 'z',
#     '-42': 'a',
#     '-39': 'f',
#     '-36': 'p',
#     '-33': 'n',
#     '-30': 'u',
#     '-27': 'm',
#     '-24': '',
#     '-21': 'k',
#     '-18': 'M',
#     '-15': 'G',
#     '-12': 'T'
# }
#
#
# class EngUnit:
#     """
#     Represents an engineering number, complete with units
#     """
#
#     def __init__(self, value,
#                  precision=2, significant=0):
#         """
#         Initialize engineering with units
#         :param value: the desired value in the form of a string, int, or float
#         :param precision: the number of decimal places
#         :param significant: the number of significant digits
#         if given, significant takes precendence over precision
#         """
#         suffix_keys = [key for key in _suffix_lookup.keys() if key != '']
#         self.unit = None
#
#         if isinstance(value, str):
#             # parse the string into unit and engineering number
#             new_value = ''
#             v_index = 0
#             for c in value:
#                 if (c in digits) or (c in ['.', '-']) or (c in suffix_keys):
#                     new_value += c
#                     v_index += 1
#                 else:
#                     break
#
#             if len(value) >= v_index:
#                 self.unit = value[v_index:]
#
#             self.eng_num = EngNumber(new_value, precision, significant)
#
#         else:
#             self.eng_num = EngNumber(value, precision, significant)
#
#     def __repr__(self):
#         """
#         Returns the object representation
#         :return: a string representing the engineering number
#         """
#         unit = self.unit if self.unit else ''
#         return str(self.eng_num) + unit
#
#     def __str__(self):
#         """
#         Returns the string representation
#         :return: a string representing the engineering number
#         """
#         return self.__repr__()
#
#     def __int__(self):
#         """
#         Implements the 'int()' method
#         :return:
#         """
#         return int(self.eng_num)
#
#     def __float__(self):
#         """
#         Implements the 'float()' method
#         :return:
#         """
#         return float(self.eng_num)
#
#     def __add__(self, other):
#         """
#         Add two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return EngUnit(str(self.eng_num + other.eng_num) + self.unit)
#
#     def __radd__(self, other):
#         """
#         Add two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         """
#         Subtract two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return EngUnit(str(self.eng_num - other.eng_num) + self.unit)
#
#     def __rsub__(self, other):
#         """
#         Subtract two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return EngUnit(str(other.eng_num - self.eng_num) + self.unit)
#
#     def __mul__(self, other):
#         """
#         Multiply two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         return EngUnit(str(self.eng_num * other.eng_num)
#                        + self.unit + other.unit)
#
#     def __rmul__(self, other):
#         """
#         Multiply two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         """
#         Divide two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         new_unit = ''
#         if self.unit:
#             new_unit += self.unit
#         if other.unit:
#             new_unit += '/' + other.unit
#
#         return EngUnit(str(self.eng_num / other.eng_num) + new_unit)
#
#     def __rtruediv__(self, other):
#         """
#         Divide two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         return EngUnit(str(other.eng_num / self.eng_num)
#                        + (other.unit + '/' + self.unit))
#
#     def __lt__(self, other):
#         """
#         Compare two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return self.eng_num < other.eng_num
#
#     def __gt__(self, other):
#         """
#         Compare two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return self.eng_num > other.eng_num
#
#     def __le__(self, other):
#         """
#         Compare two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return self.eng_num <= other.eng_num
#
#     def __ge__(self, other):
#         """
#         Compare two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return self.eng_num >= other.eng_num
#
#     def __eq__(self, other):
#         """
#         Compare two engineering numbers, with units
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, (EngNumber, EngUnit, str, int, float)):
#             return NotImplemented
#         if not isinstance(other, EngNumber):
#             other = EngUnit(str(other))
#
#         if self.unit != other.unit:
#             raise AttributeError('units do not match')
#
#         return self.eng_num == other.eng_num
#
#
# class EngNumber:
#     """
#     Used for easy manipulation of numbers which use engineering notation
#     """
#
#     def __init__(self, value,
#                  precision=2, significant=0):
#         """
#         Initialize the class
#
#         :param value: string, integer, or float representing
#         the numeric value of the number
#         :param precision: the precision past the decimal - default to 2
#         :param significant: the number of significant digits
#         if given, significant takes precendence over precision
#         """
#         self.precision = precision
#         self.significant = significant
#
#         if isinstance(value, str):
#             suffix_keys = [key for key in _suffix_lookup.keys() if key != '']
#
#             for suffix in suffix_keys:
#                 if suffix in value:
#                     value = value[:-1] + _suffix_lookup[suffix]
#                     break
#
#             self.number = Decimal(value)
#
#         elif (isinstance(value, int)
#               or isinstance(value, float)
#               or isinstance(value, EngNumber)):
#             self.number = Decimal(str(value))
#
#     def to_pn(self, sub_letter=None):
#         """
#         Returns the part number equivalent.  For instance,
#         a '1k' would still be '1k', but a
#         '1.2k' would, instead, be a '1k2'
#         :return:
#         """
#         string = str(self)
#         if '.' not in string:
#             return string
#
#         # take care of the case of when there is no scaling unit
#         if not string[-1].isalpha():
#             if sub_letter is not None:
#                 return string.replace('.', sub_letter)
#
#             return string
#
#         letter = string[-1]
#         return string.replace('.', letter)[:-1]
#
#     def __repr__(self):
#         """
#         Returns the string representation
#         :return: a string representing the engineering number
#         """
#         # since Decimal class only really converts number that are very small
#         # into engineering notation, then we will simply make all number a
#         # small number and take advantage of Decimal class
#         num_str = self.number * Decimal('10e-25')
#         num_str = num_str.to_eng_string().lower()
#
#         base, exponent = num_str.split('e')
#
#         if self.significant > 0:
#             if abs(Decimal(base)) >= 100.0:
#                 base = str(round(Decimal(base), self.significant - 3))
#             elif abs(Decimal(base)) >= 10.0:
#                 base = str(round(Decimal(base), self.significant - 2))
#             else:
#                 base = str(round(Decimal(base), self.significant - 1))
#         else:
#             base = str(round(Decimal(base), self.precision))
#
#         if 'e' in base.lower():
#             base = str(int(Decimal(base)))
#
#         # remove trailing decimals:
#         # print(base)
#         # https://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
#         # https://stackoverflow.com/questions/11227620/drop-trailing-zeros-from-decimal
#         # base = '%s' % float("%#.2G"%Decimal(base))
#         # print(base)
#         # remove trailing decimal
#         if '.' in base:
#             base = base.rstrip('.')
#
#         # remove trailing .00 in precision 2
#         if self.precision == 2 and self.significant == 0:
#             if '.00' in base:
#                 base = base[:-3]
#
#         return base + _exponent_lookup_scaled[exponent]
#
#     def __str__(self, eng=True, context=None):
#         """
#         Returns the string representation
#         :return: a string representing the engineering number
#         """
#         return self.__repr__()
#
#     def __int__(self):
#         """
#         Implements the 'int()' method
#         :return:
#         """
#         return int(self.number)
#
#     def __float__(self):
#         """
#         Implements the 'float()' method
#         :return:
#         """
#         return float(self.number)
#
#     def __add__(self, other):
#         """
#         Add two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = self.number + other.number
#         return EngNumber(str(num))
#
#     def __radd__(self, other):
#         """
#         Add two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         return self.__add__(other)
#
#     def __sub__(self, other):
#         """
#         Subtract two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = self.number - other.number
#         return EngNumber(str(num))
#
#     def __rsub__(self, other):
#         """
#         Subtract two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = other.number - self.number
#         return EngNumber(str(num))
#
#     def __mul__(self, other):
#         """
#         Multiply two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = self.number * other.number
#         return EngNumber(str(num))
#
#     def __rmul__(self, other):
#         """
#         Multiply two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         """
#         Divide two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = self.number / other.number
#         return EngNumber(str(num))
#
#     def __rtruediv__(self, other):
#         """
#         Divide two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         num = other.number / self.number
#         return EngNumber(str(num))
#
#     def __lt__(self, other):
#         """
#         Compare two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         return self.number < other.number
#
#     def __gt__(self, other):
#         """
#         Compare two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         return self.number > other.number
#
#     def __le__(self, other):
#         """
#         Compare two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         return self.number <= other.number
#
#     def __ge__(self, other):
#         """
#         Compare two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         return self.number >= other.number
#
#     def __eq__(self, other):
#         """
#         Compare two engineering numbers
#         :param other: EngNum, str, float, or int
#         :return: result
#         """
#         if not isinstance(other, (EngNumber, str, int, float)):
#             return NotImplemented
#         if not isinstance(other, EngNumber):
#             other = EngNumber(other)
#
#         return self.number == other.number

# ===========================================================================
