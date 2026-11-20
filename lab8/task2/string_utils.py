import re


def is_palindrome(s: str) -> bool:
    normalized = ''.join(s.casefold().split())
    return normalized == normalized[::-1]


def count_words(text: str) -> int:
    return len(text.split())


def truncate(text: str, max_len: int, suffix: str = '...') -> str:
    if max_len < 0:
        raise ValueError('Довжина не може бути від’ємною')
    if len(text) <= max_len:
        return text
    if len(suffix) >= max_len:
        return suffix[:max_len]
    return text[:max_len - len(suffix)] + suffix


def to_snake_case(s: str) -> str:
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return re.sub(r'[\s_-]+', '_', s.strip()).strip('_').lower()
