# This is Reva Adi's encode and main logic:
def encode(password):
    res = ""
    for num in range(len(password)):
        value = int(password[num])
        new_value = (value + 3) % 10
        res += str(new_value)
    return res


def decode():
    pass


def main():
    encode_decode_menu = True

    while encode_decode_menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit ")

        menu_selection = int(input("Please enter an option:"))
        if menu_selection == 1:
            password_response = str(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            print(encode(password_response))


if __name__ == "__main__":
    main()
