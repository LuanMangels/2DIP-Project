#Password Manneger Task V2
#In this version I coded in a way for the user to save their passwords
#Luan Mangels

print(">>> Greetings user, thank you for trusting this program to save your passwords.")

def menu():
    
    mode = input(""">>> Please select a mode by entering a number:
    1: Add new password 2: Edit a password 3: View saved passwords 4: End program :""").strip()
    return mode

def add_password():
    while True:
        add_password = input(">>> Enter a password or type 'return' to go back to the menu: ").strip().lower()
        if add_password == "return":
            break
        else:
            password_list.append(add_password)
        
password_list = []

while True:
    chosen_option = menu()
    
    if chosen_option == "1":
        add_password()
    
    elif chosen_option == "2":
        print(">>> This will edit a password in the future")
    
    elif chosen_option == "3":
        print(">>> This will let you see your passwords in the future")
    
    elif chosen_option == "4":
        break
    
    else:
        print(">>> Please enter a valid number or option")




print(">>> Thank you for your time, Goodbye.")




