import datetime



accoun_blance=100

def display_action():
    print("mohamed@diyeeshepoi                      /home")
    print("welcome to the atm")
    print("   1. With drawel")
    print("   2. Deposit")
    print("   3.Account Blance")
    print("   4.Change Pin")
    print("   5.Exit And Logout")


def usr_input():
    choice='moha'
    acceptable_range=range(0,6)
    out_range= False
    while choice.isdigit()==False and out_range ==False :
        choice=input("Enter choice :  ")
        if choice.isdigit()==False :
            print("that is not valid please enter valid number")
        if choice.isdigit()==True :
            if int(choice) in acceptable_range:
                out_range ==True
            else :
                print("that is not valid please enter valid number")
                out_range ==False

    return int (choice)

def with_drawel(amount):
    global accoun_blance
    if amount <= accoun_blance:
        print(f"you have been successfully drawe:  {amount}")
        return True
    else:
        print(f"insufficient Blance")
        return False


def depost_money(amount):
    global accoun_blance
    amount +=accoun_blance
    print(f"you have beeen successfully deposit! Current balance:  {amount}")



def account_check():
    print(f"your account blance is:  {accoun_blance}")


def transaction_file(transaction_details):
    with open('transaction_log1.txt','a') as file:
        file.write(transaction_details + "\n")


while True:
    display_action()
    user_choice=usr_input()

    if user_choice==1:
        amount=float(input("enter the amount you want to with draw :  "))
        success = with_drawel(amount)
        if success:
            transaction_details=f"{datetime.datetime.now()}: with drawel of: {amount}"
            transaction_file(transaction_details)
    elif user_choice==2:
        amount = float(input("enter the amount you want to deposit your account :  "))
        success = depost_money(amount)
        transaction_details = f"{datetime.datetime.now()}: You have deposit: {amount}"
        transaction_file(transaction_details)

    elif user_choice==3:
        account_check()
        break

    elif user_choice==4:
        print("this function is not ready now")
        break

    elif user_choice==5:
        print("you have been succesfully logged out and exit thank you for using our service")
        break















