import re

input_pass = input("Enter your password: ")

pass_length = len(input_pass)

if pass_length >= 8 and pass_length <= 16:
    if re.search(r"[A-Z]", input_pass):
        if re.search(r"[a-z]", input_pass):
            if re.search(r"[0-9]", input_pass):
                if re.search(r"[@#$]", input_pass):
                    print("Strong password")
                else:
                    print("Password must contain at least one special character.")
            else:
                print("Password must contain at least one digit.")
        else:
            print("Password must contain at least one lowercase letter.")
    else:
        print("Password must contain at least one uppercase letter.")
else:
    print("Password length must be between 8 and 16 characters.")