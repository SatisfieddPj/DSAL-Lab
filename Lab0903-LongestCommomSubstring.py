def solve():
    # Read inputs
    s1 = input().strip()
    s2 = input().strip()
    
    if not s1 or not s2:
        return

    n = len(s1)
    max_len = 0
    result_substring = ""

    # Binary Search for the maximum possible length
    low = 1
    high = n
    
    while low <= high:
        mid = (low + high) // 2
        found_in_this_len = False
        
        # Check all substrings of current length 'mid' in s1
        for i in range(n - mid + 1):
            sub = s1[i : i + mid]
            if sub in s2:
                found_in_this_len = True
                break
        
        if found_in_this_len:
            # If we found a match, try a longer length
            max_len = mid
            low = mid + 1
        else:
            # If no match, we must try a shorter length
            high = mid - 1

    # Final Step: Find the FIRST occurrence of the max_len found
    if max_len == 0:
        print("No common substring.")
    else:
        # We search s1 from left to right to guarantee the "first" found
        for i in range(n - max_len + 1):
            sub = s1[i : i + max_len]
            if sub in s2:
                print(sub)
                print(max_len)
                break

solve()