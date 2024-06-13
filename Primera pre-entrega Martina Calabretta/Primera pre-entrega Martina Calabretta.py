User_database = {}

def input_user_data():
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    User_database[Username] = Password

def show_data():
    for user in User_database.keys():
        print("Username: " + user + ", Password: " + User_database[user])

def login():
    username_input = input("Enter your username: ")
    if User_database.get(username_input) == None:
        while User_database.get(username_input) == None:
            username_input = input("Incorrect Username, please enter again: ")
        print("Correct Username!")
    password_input = input("Enter your password: ")
    while password_input != User_database[username_input]:
        password_input = input("Incorrect Password, please enter a new password: ")
    print("Correct Password!")
    print("You have successfully logged in!")

print("User Data Input")
input_user_data()
input_user_data()
input_user_data()

print("User Data Display")
show_data()

print("User Login")
login()

with open("username.txt", "w") as usernametxt:
    for user in User_database.keys():
        usernametxt.write(user)
    for password in User_database.values():
        usernametxt.write(password)