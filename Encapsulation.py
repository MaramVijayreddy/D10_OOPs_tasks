class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        if amount<=0:
            print("please enter other amount")
        else:
            self.__balance+=amount
            print("current balance",self.get_balance())
    def withdrawal(self,amount):
        if amount> self.__balance:
            print("INsuffient balance")
            print("current balance",self.get_balance())
        else:
            self.__balance-=amount
            print("current balance",self.get_balance())
    def get_balance(self):
        return self.__balance
acc=int(input("enter the account number"))
bal=int(input("enter the balance in your account"))
a=BankAccount(acc,bal)

a.deposit(int(input("enterthe amount for depositing")))
a.withdrawal(int(input("enter the amount for withdrawal")))