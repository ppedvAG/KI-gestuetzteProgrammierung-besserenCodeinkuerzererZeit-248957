from datetime import datetime
from transaction import Transaction  # Import der Transaction-Klasse

class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []  # Liste für Transaktionen

    def deposit(self, amount: float):
        self.balance += amount
        # Neue Transaktion erstellen und speichern
        transaction = Transaction(datetime.now(), self, "deposit", amount)
        self.transactions.append(transaction)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Der Abhebungsbetrag muss positiv sein.")
        if amount > self.balance:
            raise ValueError("Nicht genügend Guthaben auf dem Konto.")
        self.balance -= amount
        # Neue Transaktion erstellen und speichern
        transaction = Transaction(datetime.now(), self, "withdrawal", amount)
        self.transactions.append(transaction)

    def get_balance(self) -> float:
        return self.balance
