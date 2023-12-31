import os
import time
import random
import sys


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


account_file = "atm_pin.txt"


def pinAtm():
    if os.path.exists(account_file):
        with open(account_file, 'r') as file:
            var = file.read()[12:]
            return int(var)


password = pinAtm()


# ATM balance function
def load_balance():
    try:
        with open('atm_balance.txt', 'r') as file:
            return float(file.read())

    except FileNotFoundError:
        return 10000  # Default balance if the file doesn't exist


def save_balance(balance):
    try:
        with open('atm_balance.txt', 'w') as file:
            file.write(str(balance))

    except Exception as e:
        print(f"Error saving balance: {e}")


balance = load_balance()

# ATM pin change function


def load_account_data():
    atm_account_data = {}
    if os.path.exists(account_file):
        with open(account_file, 'r') as file:
            for line in file:
                atm_account_number, pin = line.strip().split(":")
                atm_account_data[atm_account_number] = pin
    return atm_account_data


def save_account_data(atm_account_data):
    with open(account_file, 'w') as file:
        for atm_account_number, pin in atm_account_data.items():
            file.write(f"{atm_account_number}:{pin}\n")


def change_atm_pin(atm_account_data):
    atm_account_number = input("Enter your account number: ")
    clear_console()
    if atm_account_number not in atm_account_data:
        print("Account number not found.")
        return

    print("Please enter your existing PIN number again: ")
    current_pin = input()
    clear_console()
    stored_pin = atm_account_data[atm_account_number]

    if current_pin == stored_pin:
        print("Please Wait...")
        time.sleep(2)
        clear_console()
        print("Please enter your new PIN")
        new_pin = input()
        clear_console()
        print("Please Wait...")
        time.sleep(2)
        clear_console()
        print("Please re-enter your new PIN")
        confirm_new_pin = input()
        clear_console()
        print("Your Transaction is being Processed Please wait")
        time.sleep(random.randint(4, 7))
        clear_console()
        if new_pin == confirm_new_pin:
            atm_account_data[atm_account_number] = new_pin
            save_account_data(atm_account_data)
            print("Your PIN has been changed")
        else:
            print("PINs do not match. Try again.")
    else:
        print("Incorrect existing PIN. PIN change failed.")


# bKash balance function
def check_balance():
    try:
        with open("bkash_balance.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 10000


def update_balance(balance):
    with open("bkash_balance.txt", "w") as f:
        f.write(str(balance))


balance = check_balance()


# Bangladeshi phone number validation function
def valid_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number))
    if len(phone_number) != 11:
        return False
    if not (phone_number.startswith('014') or phone_number.startswith('019') or phone_number.startswith(
            '017') or phone_number.startswith('015') or phone_number.startswith('018') or phone_number.startswith(
        '016')):
        return False
    if not phone_number[3:].isdigit():
        return False
    return True


# Banglalink phone number validation function
def valid_banglalink(b_number):
    b_number = ''.join(filter(str.isdigit, b_number))
    if len(b_number) != 11:
        return False
    if not (b_number.startswith('014') or b_number.startswith('019')):
        return False
    if not b_number[3:].isdigit():
        return False
    return True


# Grameenphone phone number validation function
def valid_grameen(g_number):
    g_number = ''.join(filter(str.isdigit, g_number))
    if len(g_number) != 11:
        return False
    if not (g_number.startswith('017')):
        return False
    if not g_number[3:].isdigit():
        return False
    return True


# Teletalk phone number validation function
def valid_teletalk(t_number):
    t_number = ''.join(filter(str.isdigit, t_number))
    if len(t_number) != 11:
        return False
    if not (t_number.startswith('015')):
        return False
    if not t_number[3:].isdigit():
        return False
    return True


# Robi phone number validation function
def valid_robi(r_number):
    r_number = ''.join(filter(str.isdigit, r_number))
    if len(r_number) != 11:
        return False
    if not (r_number.startswith('018')):
        return False
    if not r_number[3:].isdigit():
        return False
    return True


# Airtel phone number validation function
def valid_airtel(a_number):
    a_number = ''.join(filter(str.isdigit, a_number))
    if len(a_number) != 11:
        return False
    if not (a_number.startswith('018')):
        return False
    if not a_number[3:].isdigit():
        return False
    return True


account_fileB = "bkash_pin.txt"

def pinBkash():
    if os.path.exists(account_fileB):
        with open(account_fileB, 'r') as f:
            var = f.read()[12:]
            return int(var)
    
user_pin = pinBkash()


def load_user_data():
    try:
        with open(account_fileB, 'r') as f:
            return dict(line.strip().split(':') for line in f)
    except FileNotFoundError:
        return {}


def save_user_data(users):
    with open(account_fileB, "w") as f:
        for mobile, pin in users.items():
            f.write(f"{mobile}:{pin}\n")


def reset_pin():
    users = load_user_data()
    mobile_number = input("Enter your mobile number: ")
    if mobile_number not in users:
        print("Mobile number not found.")
        return
    new_pin = input("Enter your new PIN: ")
    confirm_pin = input("Confirm your new PIN: ")
    if new_pin != confirm_pin:
        print("PINs do not match. Please try again.")
        return
    users[mobile_number] = new_pin
    if new_pin != confirm_pin:
        print("PINs do not match. Please try again.")
        return
    users[mobile_number] = new_pin
    save_user_data(users)
    print("PIN reset successful!")


def download_animation():
    animation_chars = ['|', '/', '-', '\\']

    for i in range(10):
        for char in animation_chars:
            sys.stdout.write(f'\rDownloading... {char}')
            sys.stdout.flush()
            time.sleep(0.1)

    print("\nDownload complete!")


if __name__ == "__main__":

    clear_console()
    print('''
       =============================== 
      |                               |
      |  Menu:                        |
      |  1. ATM                       |
      |  2. BKASH                     |
      |                               |
       ===============================''')
    try:
        method = int(input('''
      ----------------------
      Select Your Option: '''))

        # This is for ATM
        if method == 1:
            clear_console()

            print('''
        ------------------------
        Please insert your Card
        ------------------------''')

            time.sleep(2)  # Delay to read card
            clear_console()
            print('''
        ---------------
        Welcome to ATM
        ---------------''')
            time.sleep(2)
            clear_console()

            print("Please wait, Chip data is reading from Card")
            time.sleep(4)
            clear_console()

            pin = int(
                input('''
        ----------------------------------
        Please enter your PIN number: '''))
            clear_console()

            if pin == password:

                while True:
                    print('''

         ______________________________________
        |                                      |
        |      Please select you option        |
        |                                      |
        |       1 - WITHDRAWAL                 |
        |       2 - BALANCE | STATEMENT        |
        |       3 - FUND TRANSFER              |
        |       4 - PRE-PAID CARD              |
        |       5 - FAST CASH                  |
        |       6 - PIN CHANGE                 |
        |       7 - REMITTANCE                 |
        |       8 - BILLS / FEES / TOPUP       |
        |       9 - EXIT                       |
        |______________________________________|''')

                    try:
                        option = int(input('''
        -----------------
        Enter a choice: '''))
                        clear_console()

                        if option == 2:
                            print("1. BALANCE INQUIRY")
                            print("2. MINI STATEMENT")
                            balance_statement = int(input("Enter: "))
                            clear_console()
                            if balance_statement == 1 or balance_statement == 2:
                                print("Do you want a printed receipt ?")
                                print("(Receipt paper is chargable @ Tk.3/=)")
                                print("1. Yes")
                                print("2. No")
                                answer = int(input("Enter: "))
                                clear_console()
                                print("Please Wait...")
                                time.sleep(2)
                                clear_console()
                                print("Your Transaction is being Processed Please wait")
                                time.sleep(random.randint(2, 4))
                                clear_console()
                                if answer == 1:
                                    print("Your account balance")
                                    balance -= 3
                                    save_balance(balance)
                                    print(f"AVAIL BAL TK:    {balance}")
                                elif answer == 2:
                                    print("Your account balance")
                                    save_balance(balance)
                                    print(f"AVAIL BAL TK:    {balance}")
                                else:
                                    print("Invalid number entered")
                                    break

                        elif option == 1 or option == 5:
                            print("Please enter the amount in multiples of Tk. 500")
                            withdraw_amount = float(input("Tk. "))
                            clear_console()

                            print("Do you want a printed receipt ?")
                            print("(Receipt paper is chargable @ Tk.3/=)")
                            print("1. Yes")
                            print("2. No")
                            answer = int(input("Enter: "))
                            clear_console()
                            print("Please Wait...")
                            time.sleep(2)
                            clear_console()
                            print("Your Transaction is being Processed Please wait")
                            time.sleep(random.randint(2, 4))
                            clear_console()

                            if answer == 1:
                                if withdraw_amount <= balance:
                                    balance -= withdraw_amount
                                    balance -= 3
                                    save_balance(balance)

                                    print("\t----------------------------------------")
                                    print(f"\t- You withdraw {withdraw_amount} TK✅")
                                    print(f"\t- Your current balance is {balance} TK")
                                    print("\t----------------------------------------")

                                else:
                                    print("Insufficient funds...⚠️")

                            elif answer == 2:
                                if withdraw_amount <= balance:
                                    balance -= withdraw_amount
                                    save_balance(balance)

                                    print("\t----------------------------------------")
                                    print(f"\t- You withdraw {withdraw_amount} TK✅")
                                    print(f"\t- Your current balance is {balance} TK")
                                    print("\t----------------------------------------")

                                else:
                                    print("Insufficient funds...⚠️")
                            else:
                                print("Invalid number entered")
                                break

                        elif option == 3:
                            print("Please select your option")
                            print("1. WITHIN ACCOUNT")
                            print("2. THIRD PARTY ACCOUNT")
                            answer = int(input("Enter: "))
                            clear_console()
                            print("Please Wait...")
                            time.sleep(random.randint(1, 2))
                            clear_console()
                            print("Please type the account no.")
                            account_number = float(input("ACCOUNT NUMBER: "))
                            clear_console()
                            print("Please enter the amount details")

                            fund_transfer = float(input("Tk. "))
                            clear_console()
                            print("Do you want a printed receipt ?")
                            print("(Receipt paper is chargable @ Tk.3/=)")
                            print("1. Yes")
                            print("2. No")
                            answer = int(input("Enter: "))
                            clear_console()
                            print("Please Wait...")
                            time.sleep(2)
                            clear_console()
                            print("Your Transaction is being Processed Please wait")
                            time.sleep(random.randint(2, 4))
                            clear_console()

                            if answer == 1:
                                if fund_transfer > 0:
                                    balance -= fund_transfer
                                    balance -= 3
                                    save_balance(balance)

                                    print("\t----------------------------------------")
                                    print(f"\t- You transfered {fund_transfer} Tk✅")
                                    print(f"\t- Your current balance is {balance} Tk")
                                    print("\t----------------------------------------")
                            elif answer == 2:
                                if fund_transfer > 0:
                                    balance -= fund_transfer
                                    save_balance(balance)

                                    print("\t----------------------------------------")
                                    print(f"\t- You transfered {fund_transfer} Tk✅")
                                    print(f"\t- Your current balance is {balance} Tk")
                                    print("\t----------------------------------------")

                                else:
                                    print('''
          ----------------------------                        
          Invalid deposit amount...
          ----------------------------''')
                            else:
                                print("Invalid number entered")
                                break

                        elif option == 4 or option == 7 or option == 8:
                            print("Currently this is not available for you")

                        elif option == 6:
                            account_data = load_account_data()
                            change_atm_pin(account_data)

                        elif option == 9:
                            print('''
        ----------------------------------------                    
        Thank you for using the 🏧. Goodbye!👋
        ----------------------------------------''')
                            break

                        else:
                            print('''
        --------------------------------------                    
        Invalid option. Please try again...🔄
        --------------------------------------''')
                            break

                    except ValueError:
                        print('''
        ---------------------------------------                
        Invalid... Please enter a valid number
        ---------------------------------------''')

                    print("Would you like to do another transaction ?")
                    print("1. Yes")
                    print("2. No")
                    another_transaction = int(input("Enter: "))
                    clear_console()
                    if another_transaction == 2:
                        break

            else:
                print('''
        ---------------        
        Wrong pin!!!❎
        ---------------''')

        # This is for bKash
        elif method == 2:
            clear_console()
            print('''
          \tCarrier info

    ==========================================
    ||                                      ||
    ||\tbKash                               ||
    ||\t1.send money                        ||
    ||\t2.send money to non-bkash user      ||
    ||\t3.mobile recharge                   ||
    ||\t4.payment                           ||
    ||\t5.cash out                          ||
    ||\t6.Bill                              ||
    ||\t7.Download Bkash App                ||
    ||\t8.My Bkash                          ||
    ||\t9.Reset PIN                         ||
    ||\t0.Check Balance                     ||
    ||                                      ||
    ==========================================''')

            user_input = int(input('''
    ----------------------                   
    Enter your choice : '''))

            if user_input == 1:
                clear_console()
                number = input('''

    Enter Receiver bKash Account No: ''')
                clear_console()

                if valid_phone_number(number):
                    Amount = int(input("  \nEnter Amount: "))
                    clear_console()
                    Reference = int(input("  \nEnter Reference: "))
                    clear_console()
                    Pin = int(input("  \nEnter Menu Pin: "))
                    if Pin == user_pin:
                        clear_console()
                        if Amount <= balance:
                            balance -= Amount
                            update_balance(balance)
                            print("  \nCongratulations you have successfully send money.😀\n  Number:",
                                  number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                        else:
                            print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                    else:
                        clear_console()
                        print('\t==========================')
                        print('\t\t\tWrong pin😔')
                        print('\t==========================')
                else:
                    print('''
    --------------------------------
    The bkash Account No is invalid.
    --------------------------------''')

            elif user_input == 2:
                clear_console()
                number = input('''

    Enter Receiver bKash Account No: ''')
                clear_console()

                if valid_phone_number(number):
                    Amount = int(input("  \nAmount: "))
                    clear_console()
                    Reference = int(input("  \nReference: "))
                    clear_console()
                    pin = int(input("  \nEnter Menu Pin: "))
                    if pin == user_pin:
                        clear_console()
                        if Amount <= balance:
                            balance -= Amount
                            update_balance(balance)
                            print("  \nCongratulations😀\n  Send Money to non-bkash user is Successful. \n  Number:",
                                  number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                        else:
                            print('''
    -----------------------------                
    You do not have enough money.
    -----------------------------''')
                    else:
                        clear_console()
                        print('\t=============================================')
                        print('\t\t\tWrong pin😔')
                        print('\t=============================================')
                else:
                    print('''
    --------------------------------            
    The bkash Account No is invalid.
    --------------------------------''')

            elif user_input == 3:

                clear_console()
                print("\n  1. Banglalink")
                print("  2. GrameenPhone")
                print("  3. Teletalk")
                print("  4. Robi")
                print("  5. Airtel")

                user_sim = int(input('''
    -------------------                         
    Select Your Sim: '''))

                if user_sim == 1:
                    clear_console()
                    b_number = input("\n  Enter Banglalink Number: ")
                    clear_console()

                    if valid_banglalink(b_number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))

                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                                      b_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------                  
    You do not have enough money.
    -----------------------------''')

                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    ----------------------------------              
    Invalid Banglalink Number Entered.
    ----------------------------------''')

                elif user_sim == 2:

                    clear_console()
                    g_number = input("\n  Enter GrameenPhone Number: ")
                    clear_console()

                    if valid_grameen(g_number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))

                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                                      g_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    ------------------------------------              
    Invalid Grameenphone number entered.
    ------------------------------------''')

                elif user_sim == 3:
                    clear_console()
                    t_number = input("\n  Enter Teletalk Number: ")
                    clear_console()

                    if valid_teletalk(t_number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))

                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                                      t_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    --------------------------------              
    Invalid Teletalk number entered.
    --------------------------------''')

                elif user_sim == 4:
                    clear_console()
                    r_number = input("\n  Enter Robi Number: ")
                    clear_console()

                    if valid_robi(r_number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))

                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                                      r_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    ----------------------------              
    Invalid Robi number entered.
    ----------------------------''')

                elif user_sim == 5:
                    clear_console()
                    a_number = input("\n  Enter Airtel Number: ")
                    clear_console()

                    if valid_airtel(a_number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))

                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations😀\n  Mobile Recharge SuccessFully. \n  Number:",
                                      a_number, "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    ----------------------------              
    Invalid Airtel number entered.
    ----------------------------''')

            elif user_input == 4:
                clear_console()
                number = input("\n  Enter Your Merchant Account: ")
                clear_console()

                if valid_phone_number(number):
                    Amount = int(input("\n  Enter Your Amount: "))
                    clear_console()
                    Reference = int(input("\n  Enter Reference: "))
                    clear_console()
                    pin = int(input("\n  Enter Menu PIN to confirm: "))
                    if pin == user_pin:
                        clear_console()
                        if Amount <= balance:
                            balance -= Amount
                            update_balance(balance)
                            print("  \nCongratulations\n  Your Payment is successfull. \n  To:", number,
                                  "\n  Amount:", Amount, "\n  Current Amount:", balance)
                        else:
                            print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                    else:
                        clear_console()
                        print('\t=============================================')
                        print('\t\t\tWrong pin😔')
                        print('\t=============================================')
                else:
                    print('''
    --------------------------------              
    The bkash Account No is invalid.
    --------------------------------''')

            elif user_input == 5:
                clear_console()
                print('''
    ---------------------------------------------
    Only Agent Number can transfer money.
    If you are agreed please enter either 1 or 2''')
                user_decision = int(input("  "))
                if user_decision == 1:
                    clear_console()
                    number = input("\n  Enter Receiver Number: ")
                    clear_console()

                    if valid_phone_number(number):
                        Amount = int(input("\n  Enter Amount: "))
                        clear_console()
                        pin = int(input("\n  Enter Menu PIN to confirm: "))
                        if pin == user_pin:
                            clear_console()
                            if Amount <= balance:
                                balance -= Amount
                                update_balance(balance)
                                print("  \nCongratulations\n  Your Cash Out is successful. \n  To:", number,
                                      "\n  Amount:", Amount, "\n  Current Amount:", balance)
                            else:
                                print('''
    -----------------------------
    You do not have enough money.
    -----------------------------''')
                        else:
                            clear_console()
                            print('\t=============================================')
                            print('\t\t\tWrong pin😔')
                            print('\t=============================================')
                    else:
                        print('''
    --------------------------------              
    The bkash Account No is invalid.
    --------------------------------''')

                elif user_decision == 2:
                    clear_console()

            elif user_input == 6:
                clear_console()
                print("\t\t 1.Electricity")
                print("\t\t 2.Gas")
                print("\t\t 3.Water")
                print("\t\t 4.Internet and Phone")
                payBillInput = int(input("Select Bill: "))
                if payBillInput == 1:
                    clear_console()
                    print("\t\t 1.Palli Bidyut")
                    print("\t\t 2.DESCO")
                    billType = int(input("Select Bill Type: "))
                    if billType == 1:
                        clear_console()
                        print("\t\t Palli Bidyut")
                        print("\t\t 1.Bill Breakdown")
                        print("\t\t 2.Make Payment")
                        paymentBill = int(input("Select One: "))
                        if paymentBill == 1:
                            clear_console()
                            print("\t\t Bill Breakdown")
                            print("\t\t 1.Input Meter Number")
                            print("\t\t 2.Saved Account")
                            paymentMethod = int(input("Select One: "))
                            if paymentMethod == 1:
                                clear_console()
                                meterNumber = int(input('Meter Number:'))
                                Amount = int(input('Enter Amount:'))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    if Amount <= balance:
                                        balance -= Amount
                                        update_balance(balance)
                                        print(
                                            "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif paymentMethod == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentBill == 2:
                            clear_console()
                            print("\t\t Make Payment")
                            print("\t\t 1.Input Meter Number")
                            print("\t\t 2.Saved Account")
                            paymentMethod = int(input("Select One: "))
                            if paymentMethod == 1:
                                clear_console()
                                meterNumber = int(input('Meter Number:'))
                                Contact = int(input('Contact Number:'))
                                Amount = int(input('Enter Amount:'))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    if Amount <= balance:
                                        balance -= Amount
                                        update_balance(balance)
                                        print(
                                            "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif paymentMethod == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif billType == 2:
                        clear_console()
                        print("\t\t DESCO")
                        print("\t\t 1.Bill Breakdown")
                        print("\t\t 2.Make Payment")
                        paymentBill = int(input("Select One: "))
                        if paymentBill == 1:
                            clear_console()
                            print("\t\t Bill Breakdown")
                            print("\t\t 1.Input A/C Number")
                            print("\t\t 2.Saved Account")
                            paymentMethod = int(input("Select One: "))
                            if paymentMethod == 1:
                                clear_console()
                                accountNumber = int(input('Enter Account Number:'))
                                Amount = int(input('Enter Amount:'))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    if Amount <= balance:
                                        balance -= Amount
                                        update_balance(balance)
                                        print(
                                            "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif paymentMethod == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif billType == 2:
                        clear_console()
                        print("\t\t DESCO")
                        print("\t\t 1.Bill Breakdown")
                        print("\t\t 2.Make Payment")
                        paymentBill = int(input("Select One: "))
                        if paymentBill == 1:
                            clear_console()
                            print("\t\t Bill Breakdown")
                            print("\t\t 1.Input A/C Number")
                            print("\t\t 2.Saved Account")
                            paymentMethod = int(input("Select One: "))
                            if paymentMethod == 1:
                                clear_console()
                                accountNumber = int(input('Enter Account Number:'))
                                Amount = int(input('Enter Amount:'))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    if Amount <= balance:
                                        balance -= Amount
                                        update_balance(balance)
                                        print(
                                            "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                        elif billType == 2:
                            clear_console()
                            print("\t\t Make Payment")
                            print("\t\t 1.Input Account Number")
                            print("\t\t 2.Saved Account")

                            paymentMethod = int(input("Select One: "))
                            if paymentMethod == 1:
                                clear_console()
                                meterNumber = int(input('Enter Account Number:'))
                                Contact = int(input('Contact Number:'))
                                Amount = int(input('Enter Amount:'))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    if Amount <= balance:
                                        balance -= Amount
                                        update_balance(balance)
                                        print(
                                            "Your Palli Bidyut Pay Bill is done😀. Your New balance is", balance)
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif paymentMethod == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                elif payBillInput == 2:
                    clear_console()
                    print("\t\t Gas")
                    print("\t\t 1.Jalalabad Gas")
                    print("\t\t 2.Sundarban Gas")
                    print("\t\t 3.Paschimanchan Gas")
                    print("\t\t 4.Karnaphuli Gas")
                    gas_name = int(input("Select Your Gas: "))
                    if gas_name == 1:
                        clear_console()
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")
                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Customer Code Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Input Grahok Shonket No. "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif gas_name == 2:
                        clear_console()
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Customer Code Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Input Grahok Shonket No. "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif gas_name == 3:
                        clear_console()
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Customer Code Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Input Grahok Shonket No. "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif gas_name == 4:
                        clear_console()
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Customer Code & Mobile No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter Customer Code & Mobile No. "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Grahok Shonket No.")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Input Grahok Shonket No. "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Gas Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                elif payBillInput == 3:
                    clear_console()
                    print("\t\t Water")
                    print("\t\t 1.Dhaka WASA")
                    print("\t\t 2.Chattogram WASA")
                    print("\t\t 3.Rajshahi WASA")
                    print("\t\t 4.Khulna WASA (Metered)")

                    waterBill = int(input("Enter Your Bill"))
                    if waterBill == 1:
                        clear_console()
                        print("\t\t Dhaka WASA")
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Bill Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter Bill Number"))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif waterBill == 2:
                        clear_console()
                        print("\t\t Chattogram WASA")
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Bill Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter Bill Number"))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif waterBill == 3:
                        clear_console()
                        print("\t\t Rajshahi WASA")
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Bill Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter Bill Number"))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                    elif waterBill == 4:
                        clear_console()
                        print("\t\t Khulna Wasa")
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Bill Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input Bill Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter Bill Number"))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Water Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                elif payBillInput == 4:
                    clear_console()
                    print("\t\t 1.BTCL")
                    internetBill = int(input("Choose one: "))
                    if internetBill == 1:
                        clear_console()
                        print("\t\t 1.Check Bill")
                        print("\t\t 2.Make Payment")

                        paymentMethod = int(input("Select Your Method: "))
                        if paymentMethod == 1:
                            clear_console()
                            print("Check Bill")
                            print("\t\t 1.Input RYYMM Area code + Phone Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter RYYMM Area code + Phone Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Internet Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")
                        elif paymentMethod == 2:
                            clear_console()
                            print("Make Payment")
                            print("\t\t 1.Input RYYMM Area code + Phone Number")
                            print("\t\t 2.Saved Accounts")
                            checkBillInput = int(input("Select One: "))
                            if checkBillInput == 1:
                                clear_console()
                                ghahokSonketNumber = int(
                                    input("Enter RYYMM Area code + Phone Number: "))
                                MonthYear = int(input("Month and Year mmyyyy: "))
                                pin = int(input("Enter Menu PIN: "))
                                if pin == user_pin:
                                    clear_console()
                                    print("Congratulations Your Internet Bill is complete!")
                                else:
                                    clear_console()
                                    print('\t=============================================')
                                    print('\t\t\tWrong pin😔')
                                    print('\t=============================================')
                            elif checkBillInput == 2:
                                clear_console()
                                print("Sorry, There is no beneficiary")

            elif user_input == 7:
                clear_console()
                download_animation()

            elif user_input == 8:
                clear_console()
                print("\t\t 1.Check Balance")
                print("\t\t 2.Request Statement")
                print("\t\t 3.Change PIN")

                bkashInput = int(input("Choose one: "))
                if bkashInput == 1:
                    clear_console()
                    pin = int(input("\n  Enter Menu PIN: "))
                    if pin == user_pin:
                        clear_console()
                        print(
                            f"\n  Your current bKash Account balance is\n  TK {balance}. Your available bKash Account\n  balance is Tk {balance}. bKash App diye\n  balance check ekdom simple!")
                    else:
                        print("Wrong PIN.")
                elif bkashInput == 2:
                    clear_console()
                    pin = int(input("Enter Menu Pin: "))
                    if pin == user_pin:
                        clear_console()
                        print("9/1/2023 Mobile Recharge 29tk")
                        print("9/7/2023 Mobile Recharge 49tk")
                        print("9/12/2023 Cash Out 2000tk")
                        print("9/15/2023 Pay Bill 1500tk")
                        print("9/25/2023 Mobile Recharge 290tk")
                elif bkashInput == 3:
                    clear_console()
                    NationalId = int(input("\t\t Enter Your National Id Number:"))
            
            elif user_input == 9:
                clear_console()
                NationalId = int(input("\t\t Enter Your National Id Number:"))
                reset_pin()
            
            else:
                clear_console()
                print('''
    ----------------------------         
    You Entered Wrong Number😥
    ----------------------------''')
        else:
            clear_console()
            print('''
    ---------------------------        
    You Entered Wrong Number😥
    ---------------------------''')
    except:
        print('''
    -------------------     
    Invalid entered!!!
    -------------------''')
 
