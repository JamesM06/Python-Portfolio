
Allowed = False

logins = [
    ["1456", "password"],
    ["1843", "catdog2"],
    ["2564", "redmacc98"],
    ["6542", "password3"],
    ["9876", "pizzapepparoni"],
    ["1324", "odfpjhpadifj3123"],
    ["6785", "password"]
    ]

username = str(input("Usename: "))
username = username.lower().strip()
password = str(input("Password: "))
password = password.lower().strip()

checker = [username, password]
for i in logins:
    if i == checker:
        print("Access ganted!")
        Allowed = True

if Allowed == True:
    print("")
else:
    print("Your password or username is wrong.")
    exit()

