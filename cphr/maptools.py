"""
Small utilities for mapping. Mainly for purpose in the python REPL
"""
def apply_mapping(text: str, mapping: dict[str, str]) -> str:
    return ''.join(mapping.get(c, c) for c in text)
