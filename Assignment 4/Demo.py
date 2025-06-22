from banking import *

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)
acc2.withdraw(100)

save = SavingsAccount("Charlie", 1000, 0.05)
check = CheckingAccount("Dave", 500, 200)

save.apply_interest()
check.withdraw(600)

merged = acc1 + acc2

cust = Customer("Eve")
cust.add_account(acc1)
cust.add_account(save)
cust.add_account(check)

cust.transfer(acc1, save, 100)

print_account_summary(acc1)
print_account_summary(save)
print_account_summary(check)
print_account_summary(merged)

print(acc1)
print(repr(acc1))
