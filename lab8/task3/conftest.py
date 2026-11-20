import pytest
from lab8.task3.bank import BankAccount


@pytest.fixture
def account() -> BankAccount:
    return BankAccount('Костянтин')


@pytest.fixture
def funded_account() -> BankAccount:
    account = BankAccount('Костянтин')
    account.deposit(700)
    account.deposit(500)
    account.withdraw(200, '1234')
    return account
