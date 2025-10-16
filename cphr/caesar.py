import string


def caesar(text: str, shift: int, alphabet: str = string.ascii_uppercase) -> str:
    def mapping(char: str) -> str:
        if char in alphabet:
            return alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        return char

    return ''.join(map(mapping, text))
