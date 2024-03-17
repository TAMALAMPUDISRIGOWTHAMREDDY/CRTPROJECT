def display(rem_amo):
      print("The current balance in the ATM:",rem_amo) 
def check_balance(bank):
   
      print("The current balance in your bank account:",bank) 

def withdraw(amo,bank):
      if amo>bank:
            print("Your have insufficient amount to be withdraw")
      else:
            bank-=amo
            print("The amount after withdrawn:",bank)
    #return True

def deposit(bank,amo):
    bank+=amo
    print("The amount after deposited:",rem_amo)
