"""
Docstring for ex0101
"""
def main():
    """
    Docstring for main
    """
    score = []
    for _ in range(4):
        _ = score.append(float(input()))
    threeBest = 0
    for _ in range(3):
        threeBest += max(score)
        score.remove(max(score))
    print(f"{threeBest:.0f}")
main()
