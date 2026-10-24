banksystem={}
def create_account():
    accountno=input("enter account number:")
    if accountno.isdigit():#validating if  account no numeric
        if accountno not in banksystem:#checking if  acc already existing
            name=input("enter a name:")
            if name.strip() == "":#validating name not empty
                print("name should not be empty")
                create_account()
            else:
                type=input("enter account type-current or savings:").lower()
                if (type == "current") or (type=="savings"):#valindating current or savings
                    balance=input("enter a opening balance:")
                    if balance.isdigit():##validating if balance numeric and positive
                        balance=int(balance)
                        banksystem[accountno]={"name":name,"type":type,"balance":balance}
                        print("account created successfully")
                        

                    else:
                        print("enter positive numeric value for balance")
                        create_account()
                        
                else:
                    print("enter current or savings")
                    create_account()
                           
        else:
            print("account already exists")        
    else:
        print("enter numberic value for account number")
        create_account()
        


def view_account():
    print("***account details****")
    if banksystem=={}:
        print("banksystem is empty")
    else:
        for accno, accdetails in banksystem.items():
            print("**Account No:",accno)
            for accdetkey, accdetval in accdetails.items():
                print(accdetkey,":",accdetval)
            print()
                



def search_account():
    accountnoinput=input("enter account number:")
    if accountnoinput.isdigit():#validating if acc no is numeric
        if accountnoinput in banksystem:
              print("account found, Account No:", accountnoinput)
              for key, value in banksystem[accountnoinput].items():
                print(key, ":", value)
        else:
            print("account not found")
    else:
        print("please enter a numeric value")
        search_account()



def update_account():
    accnomod=input("enter the acc num to be modified:")
    if accnomod.isdigit():#validating acc no is numeric
        if accnomod  not in banksystem:
            print("account not found")
        else:
            print('''
            1)change name
            2)change account type
            ''')
   
            op=int(input("enter a option 1 or 2:"))
            match op:
                case 1:
                    newname=input("enter the new name:")
                    if newname.strip() == "":#validating name not empty
                        print("name cannot be empty")
                        update_account()
                    else:
                        banksystem[accnomod]["name"]=newname
                        print("updated successfully")
                        
                case 2:
                    newtype=input("enter the acc type current or savings:").lower()
                    if (newtype=="current") or (newtype=="savings"):#validating if current or savings
                        banksystem[accnomod]["type"]=newtype
                        print("updated successfully")
                        
                    else:
                        print("enter current or savings")
                        update_account()
                case _:
                    print("invalid option")
                    update_account()
    else:
        print("invalid input")
        update_account()


def deposit_money():
    accnomod=input("enter the acc num:")
    if accnomod.isdigit():#validating if acc no is numeric
        if accnomod in banksystem:
            depositamt=input("enter the deposit amount greater than zero")
            if depositamt.isdigit():#validating if amount is numeric
                depositamt=int(depositamt)
                if depositamt>0:#validating if amt is positive
                    banksystem[accnomod]["balance"]+=depositamt
                    print("amount deposited successfully")
                    print("current balance=",banksystem[accnomod]["balance"])
                else:
                    print("invalid amount")
                    deposit_money()#recursive calling
            else:
                print("invalid amount")
                deposit_money()   
        else:
            print("account not found")
            deposit_money()
    else:
        print("invalid input")
        deposit_money()

def withdraw_money():
    accnomod=input("enter the acc num:")
    if accnomod.isdigit():#validating if acc no is numeric
        if accnomod in banksystem:
            withdrawamt=input("enter the withdraw amount greater than zero")
            if withdrawamt.isdigit():#validating if withdraw amt is numeric
                withdrawamt=int(withdrawamt)
                if (withdrawamt>0) and (withdrawamt<=banksystem[accnomod]["balance"]):#validating if withdraw amt positive and not exceeding balance
                    banksystem[accnomod]["balance"]-=withdrawamt
                    print("withdrawal successful")
                    print("current balance=",banksystem[accnomod]["balance"])
                else:
                    print("invalid amount")
                    withdraw_money()
            else:
                print("invalid amount")
                withdraw_money()   
        else:
            print("account not found")
            withdraw_money()
    else:
        print("invalid input")
        withdraw_money()

def delete_account():
    accno=input("enter the acc num:")
    if accno.isdigit():#validating acc no is numeric
        if accno in banksystem:
            confirm=input("are you sure Y/N:").lower()
            if (confirm=="y"):
                del banksystem[accno]
                print("account successfully deleted",banksystem)
            else:
                print("account not deleted")
        else:
            print("account not found")
            delete_account()
    else:
        print("invalid input")
        delete_account()