from remainingamount import remainingamount
from passwordchecking import passwordchecking
from operationsofatm import check_balance, withdraw, deposit
from limit import limit

def main():
    rem_amo=1500000
    bank=1000
    check_balance(rem_amo)
    print("")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if passwordchecking(username, password):
        print("Authentication successful.")
        print("Choose an option:")
        print("1. Check Balance")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4.Card Type")
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                check_balance(bank)
                
            case 2:
                amo = int(input("Enter the amount to be withdrawn: "))
                withdraw(amo, bank)
      
            case 3:
                amo = int(input("Enter the amount to be deposited: "))
                if deposit(bank,amo):
                    print("Cash deposited successfully")
            case 4:
                card=input("Enter the card type you have('1.Rupay','2.Visa','3.Mastercard'):")
                cards=get_withdrawal_limit(card)
                print("limit for this card is:",cards)
                
                    
                
            case __:
                print("Authentication failed, invalid username and password")

obj=main()
