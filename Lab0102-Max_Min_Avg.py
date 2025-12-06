"""
Docstring for Lab0102-Max_Min_Avg
"""
import json
def main():
    """
    Docstring for main
    """
    my_list = json.loads(input())
    my_list_N = len(my_list)
    total = 0
    for i in range(my_list_N):
        total += my_list[i]
    avg = total / my_list_N # find average

    most = 0
    for j in range(my_list_N): # find most
        if my_list[j] > most:
            most = my_list[j]

    least = most
    for k in range(my_list_N): # find least
        if my_list[k] < least:
            least = my_list[k]

    return (round(most, 2), round(least, 2), round(avg, 2))
print(main())
