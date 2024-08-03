import random
import string

chars = list(string.ascii_lowercase) +  list(string.ascii_uppercase) +  list(string.digits) +  list(string.punctuation)

introduction = input("Welcome to password generator!\n------------ \nClick Enter to proceed further.")

def gen_password():
    password_len = int(input("What length do you want your password to be: "))
    password_count = int(input("How many passwords do you want: "))
    if password_len <= 0 or password_count <= 0:
        print("Please enter a valid number.")
        return

    for _ in range(password_count):
        password = []
        
        if password_len <= 4: 
          password.append(random.choice(string.punctuation))
          password.append(random.choice(string.ascii_lowercase))
          password.append(random.choice(string.ascii_uppercase))
          password.append(random.choice(string.digits))
      
        while len(password) < password_len:
            password.append(random.choice(chars))
       
        random.shuffle(password)
        
        password = "".join(password[:password_len])
        print("This is your generated password: ", password)

while True:
    gen_password()
    option = input("Do you want to continue generating new passwords? (Yes/No): ").capitalize()
    if option == "No":
        print("Password Generator ended.")
        break
    elif option != "Yes":
        print("Invalid input: Enter Yes or No")
        break
print("Thank you for using our password generator.")