import string
from typing import Callable, Optional


def caesar(text: str, shift: int, alphabet: str = string.ascii_uppercase, mapper: Optional[Callable[[int], int]] = None) -> str:
    if mapper is None:
        mapper = lambda n: n + shift

    def mapping(char: str) -> str:
        if char in alphabet:
            return alphabet[mapper(alphabet.index(char)) % len(alphabet)]
        return char

    return ''.join(map(mapping, text))
