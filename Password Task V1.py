#Password Manneger Task V1
#In the first version I focused on the options for the user to choose from
#Luan Mangels

print(">>> Greetings user, thank you for trusting this program to save your passwords.")

def menu():
    mode = input(""">>> Please select a mode by entering a number:
    1: Add new password 2: Edit a password 3: View saved passwords 4: End program :""").strip()
    return mode

while True:
    chosen_option = menu()
    
    if chosen_option == "1":
        print(">>> This will add a password in the future")
    
    elif chosen_option == "2":
        print(">>> This will edit a password in the future")
    
    elif chosen_option == "3":
        print(">>> This will let you see your passwords in the future")
    
    elif chosen_option == "4":
        break
    
    else:
        print(">>> Not a valid number, please try again")




print(">>> Thank you for your time, Goodbye.")

