import pytest
from lab8.task4.validators import validate_email, validate_phone, validate_password, validate_date


EMAIL_VALID = ['a@b.ua', 'user@example.com', 'first.last@site.org', 'user123@test.net', 'user+tag@site.com', 'a_b@site.ua', 'user@sub.example.com', 'test@my-site.com']
EMAIL_INVALID = ['', 'user', 'user@', '@site.com', 'user@site', 'user name@site.com', 'user@@site.com', '.user@site.com', 'user..name@site.com']
PHONE_VALID = ['+380671234567', '0671234567', '+380501234567', '0501234567', '+380931234567', '0931234567', '+380 (67) 123-45-67', '+380 (50) 123-45-67']
PHONE_INVALID = ['', '123', '+48123456789', '+38067123456', '+3806712345678', '067123456', '06712345678', '+380abcdefghi']
PASSWORD_VALID = ['Password1!', 'Abcdef2@', 'Strong33$', 'Python4%', 'Secure55&', 'Testing6*', 'GoodPass7?', 'ABCDEFG8!']
PASSWORD_INVALID = ['', 'Ab1!', 'password1!', 'Password!', 'Password1', 'abcdefgh', '12345678', '!!!!!!!!']
DATE_VALID = ['01.01.2026', '31.12.2026', '29.02.2024', '28.02.2025', '30.04.2026', '31.01.2000', '15.06.1999', '29.02.2000']
DATE_INVALID = ['', '2026-01-01', '1.01.2026', '01.1.2026', '31.04.2026', '29.02.2025', '00.01.2026', '01.13.2026', '29.02.1900']


@pytest.mark.parametrize('email, expected', [(s, True) for s in EMAIL_VALID] + [(s, False) for s in EMAIL_INVALID])
def test_validate_email(email, expected):
    assert validate_email(email) is expected


@pytest.mark.parametrize('phone, expected', [(s, True) for s in PHONE_VALID] + [(s, False) for s in PHONE_INVALID])
def test_validate_phone(phone, expected):
    assert validate_phone(phone) is expected


@pytest.mark.parametrize('pwd, expected', [(s, True) for s in PASSWORD_VALID] + [(s, False) for s in PASSWORD_INVALID])
def test_validate_password(pwd, expected):
    result = validate_password(pwd)
    assert set(result) == {'valid', 'errors'}
    assert result['valid'] is expected
    assert isinstance(result['errors'], list)
    assert bool(result['errors']) is not expected


@pytest.mark.parametrize('pwd, errors', [
    ('Ab1!', ['Мінімум 8 символів']),
    ('password1!', ['Потрібна велика літера']),
    ('Password!', ['Потрібна цифра']),
    ('Password1', ['Потрібен спецсимвол']),
    ('', ['Мінімум 8 символів', 'Потрібна велика літера', 'Потрібна цифра', 'Потрібен спецсимвол']),
])
def test_password_errors(pwd, errors):
    assert validate_password(pwd)['errors'] == errors


@pytest.mark.parametrize('date, expected', [(s, True) for s in DATE_VALID] + [(s, False) for s in DATE_INVALID])
def test_validate_date(date, expected):
    assert validate_date(date) is expected


@pytest.mark.slow
@pytest.mark.parametrize('size', [1000, 10000])
def test_large_dataset(size):
    for i in range(size):
        assert validate_email(f'user{i}@example.com')
        assert not validate_email(f'user{i}example.com')
        assert validate_phone(f'+38067{i:07d}')
        assert not validate_phone(f'+48067{i:07d}')
        assert validate_password(f'Password{i}!')['valid']
        assert not validate_password(f'password{i}')['valid']
        assert validate_date(f'{i % 28 + 1:02d}.02.2024')
        assert not validate_date(f'32.{i % 12 + 1:02d}.2024')
