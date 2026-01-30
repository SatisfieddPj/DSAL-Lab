"""
Lab0504-Calculator
"""

def calculator_presses_fast(n):
    if n == 1:
        return 1
    
    total_digits = 0
    current_digits = 1
    limit = 10
    start = 1

    while start <= n:
        end = min(n, limit - 1)
        count = end - start + 1
        total_digits += count * current_digits
        current_digits += 1
        start = limit
        limit *= 10
        
    return total_digits + n

print(calculator_presses_fast(int(input())))