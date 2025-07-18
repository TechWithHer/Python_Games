
def view():
    with open("passwords.txt", "r") as f:
        for lines in f.readlines():     
           data = lines.rstrip()
           user, pswd = data.split("|")
           print("User: ", user, "| Password: ", pswd)

def inpt():
    name = input("Account Name: ")
    password = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("Do you want to add the password or view it? inpt/view, q for exit: ")
    
    if mode == "q":
        print ("Okay Bye!")
        quit()
    elif mode == "inpt":
        inpt()  # Placeholder for adding a password, not implemented yet
    elif mode == "view":
        view()  # Placeholder for viewing the password, not implemented yet
    else:
        print("Invalid mode")
