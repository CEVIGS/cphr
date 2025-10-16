"""
Frequency analysis
"""
def get_frequencies(text: str) -> dict[str, int]:
    ret = {}
    for char in text:
        if char in ret:
            ret[char] += 1
        else:
            ret[char] = 1
    return ret
