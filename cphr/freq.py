"""
Frequency analysis
"""
from typing import Optional


def get_frequencies(text: str, allowed_chars: Optional[str] = None) -> dict[str, int]:
    """
    Counts the number of occurrences of each unique character in the text.
    :param text: String to count chars in
    :param allowed_chars: Whitelist of chars to count
    :return: A dictionary mapping each unique character to its frequency
    """
    ret = {}
    for char in text:
        if allowed_chars is not None and char not in allowed_chars:
            continue

        if char in ret:
            ret[char] += 1
        else:
            ret[char] = 1
    return ret


def get_relative_freqs(text: str, allowed_chars: Optional[str] = None) -> dict[str, float]:
    """
    Get the relative frequencies of each character in the text, i.e. the sum of all relative frequencies is 1.
    :param text: String to count chars in.
    :param allowed_chars: Whitelist of chars to check from
    :return: Relative frequencies of each character relative to the text.
    """
    return {char: count / len(text) for char, count in get_frequencies(text, allowed_chars).items()}


# https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
LETTER_FREQS = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02360,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

LETTER_FREQS_STARTING_WORDS = {
    'T': 0.1594,
    'A': 0.155,
    'I': 0.0823,
    'S': 0.0775,
    'O': 0.0712,
    'C': 0.0597,
    'M': 0.0426,
    'F': 0.0408,
    'P': 0.040,
    'W': 0.0382
}
LETTER_FREQS_ENDING_WORDS = {
    'E': 0.1917,
    'S': 0.1435,
    'D': 0.0923,
    'T': 0.0864,
    'N': 0.0786,
    'Y': 0.0730,
    'R': 0.0693,
    'O': 0.0467,
    'L': 0.0456,
    'F': 0.0408
}

# in order
MOST_COMMON_BIGRAMS = [
    'TH',
    'HE',
    'IN',
    'EN',
    'NT',
    'RE',
    'ER',
    'AN',
    'TI',
    'ES',
    'ON',
    'AT',
    'SE',
    'ND',
    'OR',
    'AR',
    'AL',
    'TE',
    'CO',
    'DE',
    'TO',
    'RA',
    'ET',
    'ED',
    'IT',
    'SA',
    'EM',
    'RO'
]
# in order
MOST_COMMON_TRIGRAMS = [
    'THE',
    'AND',
    'THA',
    'ENT',
    'ING',
    'ION',
    'TIO',
    'FOR',
    'NDE',
    'HAS',
    'NCE',
    'EDT',
    'TIS',
    'OFT',
    'STH',
    'MEN'
]

def get_letter_deviation(text: str, expected_frequencies: Optional[dict[str, float]] = None) -> float:
    """
    Get the average deviation of each character's relative frequency to its expected frequency.
    :param text: String to compare relative frequencies to.
    :param expected_frequencies: Dictionary mapping each unique character to its expected relative frequency
    :return: The mean distance to the expected frequency.
    """
    if expected_frequencies is None:
        expected_frequencies = LETTER_FREQS

    allowed_chars = ''.join(expected_frequencies.keys())
    relative_frequencies = get_relative_freqs(text, allowed_chars)
    average_deviation = 0

    # we will only check against frequencies in the expected frequencies.
    for char, expected_freq in expected_frequencies.items():
        average_deviation += abs(relative_frequencies.get(char, 0) - expected_freq)

    return average_deviation / len(expected_frequencies)

def get_closest_freq(freq: float, expected_frequencies: Optional[dict[str, float]] = None) -> str:
    if expected_frequencies is None:
        expected_frequencies = LETTER_FREQS

    return min(expected_frequencies, key=lambda k: abs(freq - expected_frequencies[k]))
