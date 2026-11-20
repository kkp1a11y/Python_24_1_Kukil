import re
import string
from datetime import datetime


def validate_email(email: str) -> bool:
    return re.fullmatch(r'[A-Za-z0-9_+%-]+(?:\.[A-Za-z0-9_+%-]+)*@[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)*\.[A-Za-z]{2,}', email) is not None


def validate_phone(phone: str) -> bool:
    return re.fullmatch(r'(?:\+380[0-9]{9}|0[0-9]{9}|\+380 \([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2})', phone) is not None


def validate_password(pwd: str) -> dict[str, bool | list[str]]:
    errors = []
    if len(pwd) < 8:
        errors.append('Мінімум 8 символів')
    if not any(c.isupper() for c in pwd):
        errors.append('Потрібна велика літера')
    if not any(c.isdigit() for c in pwd):
        errors.append('Потрібна цифра')
    if not any(c in string.punctuation for c in pwd):
        errors.append('Потрібен спецсимвол')
    return {'valid': not errors, 'errors': errors}


def validate_date(s: str) -> bool:
    if re.fullmatch(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', s) is None:
        return False
    try:
        datetime.strptime(s, '%d.%m.%Y')
    except ValueError:
        return False
    return True
