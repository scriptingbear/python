# pybank
An exercise in Python 3 scripting where the task is to implement a very basic book banking system

Here is my attempt at solving the final project challenge of implementing a banking system. I tried to identify the nouns (classes) and associated attributes (properties and methods). I ended up not having to create a User object although I thought I needed to originally. Since the specification calls for user input I guess the computer plays the role of the user.

Not sure if I implemented polymorphism correctly but the Bank class and the Account class both have similarly named methods: Deposit() and Withdraw().  For the Bank object, Deposit() validates the user and prompts for an amount and then calls the method of the same name on an Account object. The same thing happens with the Bank.Withdraw() method, which calls the Account.Withdraw() method after validating the user and prompting for an amount.

I added a PrintAllAccounts() method to see if the code is properly creating and updating the accounts.
