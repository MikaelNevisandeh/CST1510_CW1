import string
password_is_correct = False
print("=" * 40)
print ("Password validation system")
print("=" * 40)
print()
Password = input("Enter your password please:")
if len(Password) < 8:
    print("Password must be a minimum of 8 characters")
elif not any(char.isupper() for char in Password):
    print("password must contain at least one uppercase letter")
elif not any(char in string.punctuation for char in Password):
    print("password must contain at least one special character")
elif any(char.isspace() for char in Password):
    print("password must not contain any spaces")
elif not any(char.isdigit() for char in Password):
    print("password must contain at least one digit")
