user_name = input("Please create a username: ")
password = input("Please create a password: ")

file1 = open("text.txt", "a")
file1.write(user_name)
file1.write(" ")
file1.write(password)
file1.write("\n")
file1.close()

enter_user = input("Please enter your username: ")
enter_password = input("Please enter your password: ")

file2 = open('text.txt', "r")
contents = file2.read()
file2.close()

stored_credentials = contents.split("\n")

def check():
    for credentials in stored_credentials:
        if credentials:
            stored_user, stored_pass = credentials.split(" ")
            if enter_user == stored_user and enter_password == stored_pass:
                return "Welcome"
    return "Invalid username or password"

result = check()
print(result)
