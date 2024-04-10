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