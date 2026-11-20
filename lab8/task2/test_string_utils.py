import pytest
from lab8.task2.string_utils import is_palindrome, count_words, truncate, to_snake_case


@pytest.mark.parametrize('text, expected', [('', True), (' ', True), ('А роза упала на лапу Азора', True), ('Level', True), ('hello', False), ('a', True), ('ab', False)])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize('text, expected', [('', 0), ('   ', 0), ('Привіт', 1), ('Привіт світе', 2), (' один  два   три ', 3), ('a\nb\tc', 3), ('слово, слово!', 2)])
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize('text, limit, suffix, expected', [('', 5, '...', ''), ('hello', 5, '...', 'hello'), ('hello', 10, '...', 'hello'), ('hello world', 8, '...', 'hello...'), ('hello', 0, '...', ''), ('hello', 2, '...', '..'), ('hello', 3, '', 'hel'), ('abcdef', 4, '~', 'abc~')])
def test_truncate(text, limit, suffix, expected):
    result = truncate(text, limit, suffix)
    assert result == expected
    assert len(result) <= limit


def test_truncate_default_suffix():
    assert truncate('abcdef', 5) == 'ab...'


def test_truncate_negative_length():
    with pytest.raises(ValueError):
        truncate('abc', -1)


@pytest.mark.parametrize('text, expected', [('', ''), (' ', ''), ('Hello World', 'hello_world'), ('helloWorld', 'hello_world'), ('HTTPServer', 'http_server'), ('already_snake', 'already_snake'), (' Hello   World ', 'hello_world'), ('hello-world', 'hello_world'), ('Привіт світ', 'привіт_світ')])
def test_to_snake_case(text, expected):
    assert to_snake_case(text) == expected
