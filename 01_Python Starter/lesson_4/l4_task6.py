attempt = 1

login = "Sergey"
password = "1234"

while attempt < 4:
    user_login, user_pasword = input("Enter login: "), input("Enter password: ")
    if (user_login == user_login or user_pasword == password):
        print(f"You have successfully autorizated from {attempt} attempt")
        break
    else:
        attempt += 1
        print("Mistake!")
