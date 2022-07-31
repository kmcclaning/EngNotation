# Purpose

This package returns a number and optionally, the number's unit, as a string
expressed in engineering notation. The format is loosely based on the engineering
notation display of the HP-25/HP-35 calculators.

Engineering notation expresses a number in scientific notation except that
the exponent is forced to be a multiple of three. This format allows us to
use common multiplies such as 'k' for 10^3, 'u' for 10^-6, etc.

The number of digits returned is 3 + 'precision'. The precision default is 0, causing
the routine to express the number with 3 significant digits.

This module is based upon the highly-useful but more-than-I-needed package at:
https://github.com/slightlynybbled/engineering_notation

# Examples

```
# general calling procedure
eN = EngineeringNotation(thisNum, precision=precision, unitS=unitS)
print( '%s' % eN )

# prints '27.2u'
eN = EngineeringNotation(2.718281828e-05)
print( '%s' % eN )

# prints '2.72'
eN = EngineeringNotation(2.718281828)
print( '%s' % eN )

# prints '272M'
eN = EngineeringNotation( 271828182.8)
print( '%s' % eN )

# prints '42.000000000 uJ'
eN = EngineeringNotation(4.2e-05, precision=8, unitS='J')
print( '%s' % eN )

# prints '98.77 MOhm'
eN = EngineeringNotation(98765432.1, precision=1, unitS='Ohm')
print( '%s' % eN )
```
See the test file for more examples.
