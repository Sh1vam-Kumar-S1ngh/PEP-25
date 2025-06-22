class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
        else:
            print("Amount must be positive")

    def withdraw(self, amt):
        if amt > 0 and amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Invalid withdrawal amount")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_bal):
        if new_bal >= 0:
            self.__balance = new_bal
        else:
            print("Balance cannot be negative")

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"

    def __repr__(self):
        return f"<BankAccount owner={self.owner}, balance={self.__balance}>"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_owner = self.owner + " " + other.owner
            new_balance = self.__balance + other.__balance
            return BankAccount(new_owner, new_balance)
        return None


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, overdraft_limit=0.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amt):
        if amt > 0 and amt <= self.balance + self._overdraft_limit:
            self.balance = self.balance - amt
        else:
            print("Overdraft limit exceeded or invalid amount")

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, limit):
        if limit >= 0:
            self._overdraft_limit = limit
        else:
            print("Limit must be non-negative")


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = 0
        for acc in self.accounts:
            total += acc.balance
        return total

    def transfer(self, from_acc, to_acc, amt):
        from_acc.withdraw(amt)
        to_acc.deposit(amt)


def print_account_summary(obj):
    print(f"Owner: {obj.owner}, Balance: {obj.balance}")
