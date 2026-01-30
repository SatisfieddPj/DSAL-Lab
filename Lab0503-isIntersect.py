"""
Lab0503-isIntersect
"""

def isIntersect(a, b, c):
    list_a = [int(x) for x in a.replace('[', '').replace(']', '').split(',')]
    list_b = [int(x) for x in b.replace('[', '').replace(']', '').split(',')]
    list_c = [int(x) for x in c.replace('[', '').replace(']', '').split(',')]

    for num in list_a:
        if (num in list_b) and (num in list_c):
            return True
    return False

print(isIntersect(input(), input(), input()))