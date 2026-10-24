import bankfunctions

def show_menu():
    print("======SIMPLE BANKING SYSTEM======")
    print('''
          1) create account
          2)view all accounts
          3)search account
          4)update account details
          5)deposit money
          6)withdraw money
          7)delete account
          8)exit
          ''')
    choice=int(input("enter a choice:"))

    match choice:
        case 1:
            bankfunctions.create_account()
            show_menu()
        case 2:
            bankfunctions.view_account()
            show_menu()
            
        case 3:
            bankfunctions.search_account()
            show_menu()
            
        case 4:
            bankfunctions.update_account()
            show_menu()
            
        case 5:
            bankfunctions.deposit_money()
            show_menu()
        
        case 6:
            bankfunctions.withdraw_money()
            show_menu()    
        case 7:
            bankfunctions.delete_account()
            show_menu()
        case 8:
            print("thankyou for using banking system")
            exit(0)
        case _:
            print("invalid choice")
            

show_menu()   