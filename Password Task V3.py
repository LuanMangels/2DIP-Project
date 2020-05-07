#Password Manneger Task V3
#In this version I coded in a way for the user to see their saved passwords using a list
#Luan Mangels

print(">>> Greetings user, thank you for trusting this program to save your passwords.")

def menu():
    
    mode = input(""">>> Please select a mode by entering a number:
    1: Add new password 2: Edit a password 3: View saved passwords 4: End program :""").strip()
    return mode

def add_password():
    while True:
        new_password = input(">>> Enter a number to choose an option or type 'return' to go back to the menu: ").strip().lower()
        if new_password == "return":
            break
        else:
            password_list.append(new_password)
              
        
def see_passwords():
    for password in password_list:
        print(" >>> ".format(password))
        
password_list = []          

while True:
    chosen_option = menu()
    
    if chosen_option == "1":
        add_password()
    
    elif chosen_option == "2":
        print(">>> This will edit a password in the future")
    
    elif chosen_option == "3":
        see_passwords()
    
    elif chosen_option == "4":
        break
    
    else:
        print(">>> Please enter a valid number or option")




print(">>> Thank you for your time, Goodbye.")



