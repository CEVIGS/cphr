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


# https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
LETTER_FREQS = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}

LETTER_FREQS_STARTING_WORDS = {
    't': 0.1594,
    'a': 0.155,
    'i': 0.0823,
    's': 0.0775,
    'o': 0.0712,
    'c': 0.0597,
    'm': 0.0426,
    'f': 0.0408,
    'p': 0.040,
    'w': 0.0382
}
LETTER_FREQS_ENDING_WORDS = {
    'e': 0.1917,
    's': 0.1435,
    'd': 0.0923,
    't': 0.0864,
    'n': 0.0786,
    'y': 0.0730,
    'r': 0.0693,
    'o': 0.0467,
    'l': 0.0456,
    'f': 0.0408
}
