from math import isfinite
from pathlib import Path


class BankAccount:
    """Банківський рахунок із PIN-кодом і журналом операцій."""

    def __init__(self, owner: str, pin: str = '1234') -> None:
        self.owner = owner
        self.__pin = pin
        self._balance = 0.0
        self._transactions: list[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def transactions(self) -> list[str]:
        return self._transactions.copy()

    def _check_amount(self, amount: float) -> None:
        if not isfinite(amount) or amount <= 0:
            raise ValueError('Сума має бути додатною та скінченною')

    def deposit(self, amount: float) -> None:
        self._check_amount(amount)
        self._balance = round(self._balance + amount, 2)
        self._transactions.append(f'Поповнення: {amount:.2f} грн')

    def withdraw(self, amount: float, pin: str) -> None:
        if pin != self.__pin:
            raise PermissionError('Неправильний PIN')
        self._check_amount(amount)
        if amount > self._balance:
            raise ValueError('Недостатньо коштів')
        self._balance = round(self._balance - amount, 2)
        self._transactions.append(f'Зняття: {amount:.2f} грн')

    def save_statement(self, path: str | Path) -> None:
        lines = [f'Власник: {self.owner}', *self._transactions,
                 f'Баланс: {self.balance:.2f} грн']
        Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')
