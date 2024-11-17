#implement a banking system
'''REQUIREMENTS:
1. Prompt user to create new savings account or access an existing one
2. To create a new account, accept user name and generate a random
   5 digit account number
3. To access and existing account, validate user name and account
   number, then give him the option to withdraw or deposit money, or
   display the available balance.

CLASS: Account
    Attributes: account_number, type, balance
    Methods: deposit, withdraw
CLASS: User
    Attributes: name
    Methods: make_withdrawal, make_deposit
CLASS: Bank
    Attributes: name, list_of_accounts
    Methods: create_account, display_account

'''

import random, sys

class Bank:
    _accounts = {}
    _name = "PyBank Inc"

    def __init__(self):
        print("Welcome to PYBANK!")

    @property
    def Name(self):
        return Bank._name

    def CreateAccount(self):
        acct_num = self.GenerateAccountNumber()
        user_name = self.GetUserName()
        if not user_name:
            return None
        
        deposit_amt = self.GetAmount("DEPOSIT")
        if not deposit_amt:
            return
        
        account = Account(user_name, acct_num, deposit_amt)
        self._accounts[acct_num] = account
        print("Savings account #{} has been created for customer {} with opening balance of ${:,.2f}." \
              .format(account.AccountNumber, account.Name, account.Balance))
        


    def ValidateUser(self):
        user_name = self.GetUserName()
        if not user_name:
            return None
        
        acct_num = self.GetAccountNumber()
        if not acct_num:
            return None
        
        account = self._accounts.get(acct_num, None)
        
        if not account:
            print("Invalid account number.")
            return None
        elif account.Name != user_name:
            print("Invalid user name.")
            return None
        else:
            return account

        
    def DisplayBalance(self):
        account = self.ValidateUser()
        if account:
            print("Current balance  on account {} is {:,.2f}".format(account.AccountNumber, account.Balance))
        

    def Deposit(self):
        account = self.ValidateUser()
        if not account:
            return
        
        deposit_amt = self.GetAmount("DEPOSIT")
        if not deposit_amt:
            return
        
        account.Deposit(deposit_amt)
        self._accounts[account.AccountNumber] = account
        print("An deposit of ${:,.2f} has been made to account {} for a current balance of ${:,.2f}." \
              .format(deposit_amt, account.AccountNumber, account.Balance))
        

    def Withdraw(self):
        account = self.ValidateUser()
        if not account:
            return
        
        withdraw_amt = self.GetAmount("WITHDRAWAL")
        if not withdraw_amt:
            return
        
        account.Withdraw(withdraw_amt)
        self._accounts[account.AccountNumber] = account
        print("An withdrawal of ${:,.2f} has been made to account {} for a current balance of ${:,.2f}." \
              .format(withdraw_amt, account.AccountNumber, account.Balance))
        

    def GenerateAccountNumber(self):
        return random.randint(10000, 99999)

    def GetUserName(self):
        user_name = input("Enter user name: ").strip()
        if not user_name:
            print("Invalid user name")
            return None
        else:
            return user_name

    def GetAmount(self, amount_type):
        amount = input("Enter amount of " + amount_type + ": ")
        try:
            amount = float(amount)
        except Exception:
            print("Invalid input.")
            return None
        
        if amount <= 0:
            print("Invalid amount.")
            return None
        
        return amount
    
    def GetAccountNumber(self):
        acct_num = input("Enter 5 digit account number: ")
        if not acct_num.isnumeric():
            print("Invalid account number.")
            return None
        elif len(acct_num) != 5:
            print("Account number must be 5 digits")
            return None
        else:
            return int(acct_num)

    def PrintAllAccounts(self):
        format_string = "{:<10}{:30}${:<,.2f}"
        print("{:10}{:30}{:20}".format('Account', 'Name', 'Balance'))
        print('=' * 70)
        for account in self._accounts.values():
            print(format_string.format(account.AccountNumber, account.Name, account.Balance))
            
        


class Account:
    def __init__(self, name, acct_num, deposit):
        self._name = name
        self._account_number = acct_num
        self._balance = deposit
                                                                             

    @property
    def Balance(self):
        #balance is read only
        return self._balance

    @property
    def AccountNumber(self):
        #Account Number is read only
        return self._account_number
                                                                             
 
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    def Deposit(self, value):
        if value > 0:
            self._balance += value
        else:
            print("Invalid deposit amount.")

    def Withdraw(self, value):
        if value <= self._balance:
            self._balance -= value
        else:
            print("Invalid withdrawal amount.")


#instantiate bank

pybank = Bank()
menu_options = '''
Select an option:
1. Create an account
2. Make a deposit
3. Make a withdrawal
4. Display balance
5. Display all acounts
Q. Quit


'''

menu_func = ['CreateAccount', 'Deposit', 'Withdraw', 'DisplayBalance', 'PrintAllAccounts']

while True:
    choice = input(menu_options)
    if choice not in ['1', '2', '3', '4', '5', 'Q']:
        print("Invalid selection. Program terminated.")
        sys.exit(-999)
    elif choice == 'Q':
        print("Thanks for using PYBANK! Goodbye!")
        sys.exit(0)
    else:
        getattr(pybank, menu_func[int(choice) - 1])()
