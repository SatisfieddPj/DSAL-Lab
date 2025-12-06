"""
Docstring for Lab0101-Is_Even
"""

def is_even(num):
    """
    Checks whether or not the number is 
    """
    if num[-1] in ('0', '2', '4', '6', '8'):
        return "True"
    else: return "False"
print(is_even(input()))
