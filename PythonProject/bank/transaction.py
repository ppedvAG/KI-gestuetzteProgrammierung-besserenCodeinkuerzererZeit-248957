from datetime import datetime

class Transaction:
    def __init__(self, date: datetime, account, transaction_type: str, amount: float):
        # Import von BankAccount nur bei Bedarf
        from bankAccount import BankAccount
        if not isinstance(account, BankAccount):
            raise TypeError("account muss eine Instanz von BankAccount sein.")
        self.date = date
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount
