

while True:
    password = input("Enter your password: ")

    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/"

    has_special = False

    for character in password:
        if character in special_characters:
            has_special = True
            break

    if has_special:
        print("Password has a special character.")
    else:
        print("Password must contain at least one special character.")

    again = input("Try Again? (Y/N): ")

    if again.upper() == "Y":
        print("Restarting...")

    elif again.upper() == "N":
        print("ALL GOOD")
        break

    else:
        print("WRONG PASSWORD")
        break




