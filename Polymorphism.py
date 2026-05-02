class Payment:
    def __init__(self,amount):
        self.amount=amount
        
    def make_payment(self):
        print("Payment is done")
class CreditCardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def make_payment(self):
        print("Payment done by using CreditCard")
        print(f"amount:{self.amount} ")
        
        
class UPIPayment (Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def make_payment(self):
        print("Payment done by using UPIPayment ")
        print(f"amount:{self.amount} ")
        
        
class NetBankingPayment (Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def make_payment(self):
        print("Payment done by usinG NetBankingPayment ")
        print(f"amount:{self.amount} ")
        
        
def process(payment_method):
    payment_method.make_payment()
    
   
def main():
    print("1.UPIPAYMENT\n2.CreditCarPayment\n3.NetBAnking")
    typee=int(input("please choose the mode of payment"))

    if typee==1:
        amount=int(input("please enter the amount"))
        process(UPIPayment(amount))
        print("THANKYOU")
    elif typee==2:
        amount=int(input("please enter the amount"))
        process(CreditCardPayment(amount))
        print("THANKYOU")
    elif typee==3:
        amount=int(input("please enter the amount"))
        process(NetBankingPayment(amount))
        print("THANKYOU")
    else:
        print("WRONG SELECTION")

if __name__=="__main__":
    main()