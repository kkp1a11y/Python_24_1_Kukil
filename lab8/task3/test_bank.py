import pytest


class TestBankAccount:
    def test_initial_state(self, account):
        assert account.owner == 'Костянтин'
        assert account.balance == pytest.approx(0)
        assert account.transactions == []

    def test_funded_account(self, funded_account):
        assert funded_account.balance == pytest.approx(1000)
        assert len(funded_account.transactions) == 3

    @pytest.mark.parametrize('amount', [1, 100, 250.75])
    def test_deposit(self, account, amount):
        account.deposit(amount)
        assert account.balance == pytest.approx(amount)
        assert account.transactions == [f'Поповнення: {amount:.2f} грн']

    @pytest.mark.parametrize('amount', [1, 250.75, 1000])
    def test_withdraw(self, funded_account, amount):
        funded_account.withdraw(amount, '1234')
        assert funded_account.balance == pytest.approx(1000 - amount)
        assert funded_account.transactions[-1] == f'Зняття: {amount:.2f} грн'

    def test_wrong_pin(self, funded_account):
        journal = funded_account.transactions
        with pytest.raises(PermissionError, match='PIN'):
            funded_account.withdraw(100, '0000')
        assert funded_account.balance == pytest.approx(1000)
        assert funded_account.transactions == journal

    def test_insufficient_balance(self, funded_account):
        journal = funded_account.transactions
        with pytest.raises(ValueError, match='Недостатньо'):
            funded_account.withdraw(1001, '1234')
        assert funded_account.balance == pytest.approx(1000)
        assert funded_account.transactions == journal

    @pytest.mark.parametrize('amount', [0, -1, float('inf'), float('nan')])
    def test_invalid_deposit(self, account, amount):
        with pytest.raises(ValueError):
            account.deposit(amount)
        assert account.balance == pytest.approx(0)
        assert account.transactions == []

    @pytest.mark.parametrize('amount', [0, -1, float('inf'), float('nan')])
    def test_invalid_withdraw(self, funded_account, amount):
        with pytest.raises(ValueError):
            funded_account.withdraw(amount, '1234')
        assert funded_account.balance == pytest.approx(1000)
        assert len(funded_account.transactions) == 3

    def test_transaction_history(self, funded_account):
        assert funded_account.transactions == [
            'Поповнення: 700.00 грн',
            'Поповнення: 500.00 грн',
            'Зняття: 200.00 грн',
        ]

    def test_history_is_copy(self, funded_account):
        funded_account.transactions.clear()
        assert len(funded_account.transactions) == 3

    def test_save_statement(self, funded_account, tmp_path):
        path = tmp_path / 'statement.txt'
        funded_account.save_statement(path)
        assert path.read_text(encoding='utf-8') == (
            'Власник: Костянтин\n'
            'Поповнення: 700.00 грн\n'
            'Поповнення: 500.00 грн\n'
            'Зняття: 200.00 грн\n'
            'Баланс: 1000.00 грн\n'
        )
