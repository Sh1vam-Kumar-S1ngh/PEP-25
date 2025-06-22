Simple Banking System

This is a basic project I made to practice object-oriented programming in Python. It includes different types of bank accounts and a customer who can hold multiple accounts.

What I learned:

Using __init__ in classes:
I used it to set the values like owner name and balance when an account is created.

Class vs Object Variables:
I made a class variable called total_accounts to count how many accounts are made in total.

Hiding data (Encapsulation):
I used double underscore (__balance) to hide the balance. Then I used @property to access and update it safely.

Inheritance and Method Overriding:
I made SavingsAccount and CheckingAccount by extending BankAccount. I also changed how withdraw() works in the checking account so it allows overdraft.

Polymorphism:
I could call deposit, withdraw, and other methods on different account types without checking what kind of account it is.

Adding Accounts Together:
I used + to combine two accounts into a new one using the __add__ function.

Customer Class (Composition):
A customer can have multiple accounts. I stored these in a list and added functions like transfer and total_balance.

Duck Typing:
I made a function that prints owner and balance. It works for anything that has those two things, not just bank accounts.
