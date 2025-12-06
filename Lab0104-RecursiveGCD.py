"""
Docstring Lab0104-RecursiveGCD
"""

def gcd(a, b):
    """
    Docstring gcd
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print(gcd(int(input()), int(input())))
