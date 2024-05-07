from datetime import datetime

# Domain Events
class AccountCreatedEvent:
    def __init__(self, account_number):
        self.account_number = account_number

class TransactionInitiatedEvent:
    def __init__(self, transaction_id, source_account_number, destination_account_number, amount):
        self.transaction_id = transaction_id
        self.source_account_number = source_account_number
        self.destination_account_number = destination_account_number
        self.amount = amount

# Entities
class Account:
    def __init__(self, account_number, customer, account_type):
        self.account_number = account_number
        self.balance = 0.0
        self.account_type = account_type
        self.customer = customer
        self.creation_date = datetime.now()
        self.status = "Active"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.deposit(amount)
        else:
            raise ValueError("Insufficient funds")

class Customer:
    def __init__(self, customer_id, name, email, phone_number, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, source_account, destination_account):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date_time = datetime.now()
        self.source_account = source_account
        self.destination_account = destination_account

# Services
class AccountService:
    def create_account(self, customer, account_type):
        account_number = self.generate_account_number()  # Assume a method to generate unique account numbers
        account = Account(account_number, customer, account_type)
        event = AccountCreatedEvent(account_number)
        customer.add_account(account)
        return account, event

    def initiate_transaction(self, source_account, destination_account, amount):
        transaction_id = self.generate_transaction_id()  # Assume a method to generate unique transaction IDs
        transaction = Transaction(transaction_id, "Transfer", amount, source_account, destination_account)
        source_account.transfer(destination_account, amount)
        event = TransactionInitiatedEvent(transaction_id, source_account.account_number, destination_account.account_number, amount)
        return transaction, event

    # Other methods for deposit, withdrawal, etc.

    def generate_account_number(self):
        # Logic to generate unique account number
        pass

    def generate_transaction_id(self):
        # Logic to generate unique transaction ID
        pass

# Example usage:
# Instantiate services
account_service = AccountService()

# Create a customer
customer = Customer(customer_id=1, name="John Doe", email="john@example.com", phone_number="1234567890", address="123 Main St")

# Create a new account
new_account, account_created_event = account_service.create_account(customer, account_type="Savings")
new_account.deposit(1000)
print("New account created:", new_account.account_number)
print("Account created event published:", account_created_event.account_number)

# Make a transaction
destination_account = Account(account_number=2, customer=customer, account_type="Checking")
transaction, transaction_initiated_event = account_service.initiate_transaction(new_account, destination_account, amount=100)
print("Transaction initiated:", transaction.transaction_id)
print("Transaction initiated event published:", transaction_initiated_event.transaction_id)
