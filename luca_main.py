def encode_password(password):
    encoded_password =" "
    for digit in password:
        new_digit = str((int(digit)+3)%10)
        encoded_password += new_digit
    return encoded_password

def decode_password(password):
    decoded_password =" "
    for digit in password:
        new_digit = str((int(digit)-3)%10)
        decoded_password += new_digit
    return decoded_password

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

def main():
    while True:
        menu()
        x = int(input("Please enter an option: "))
        if x == 3:
            return False
        elif x == 1:
            password = input("Please enter password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode_password(password)
        elif x == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}")

if __name__ == "__main__":
    main()