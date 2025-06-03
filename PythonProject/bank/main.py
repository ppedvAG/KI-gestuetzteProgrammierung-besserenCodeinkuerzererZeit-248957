from bankAccount import BankAccount
from transaction import Transaction

def main():
    # Erstelle ein neues Bankkonto
    konto = BankAccount("123456789", 1000.0)

    # Führe einige Transaktionen durch
    konto.deposit(200.0)
    print(f"Neuer Kontostand nach Einzahlung: {konto.get_balance()} EUR")

    try:
        konto.withdraw(500.0)
        print(f"Neuer Kontostand nach Abhebung: {konto.get_balance()} EUR")
    except ValueError as e:
        print(e)

    # Zeige alle Transaktionen an
    print("Transaktionen:")
    for transaction in konto.transactions:
        print(f"{transaction.date}: {transaction.transaction_type} von {transaction.amount} EUR")

if __name__ == "__main__":
    main()
