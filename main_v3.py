# imports
import pandas
# functions

def instructions():
    print("***** INSTRUCTIONS *****")
    print('''
    Please choose whether you wish to encrypt or decrypt a message.
    
    If you choose to encrypt:
        - Enter the message you wish to encrypt
        - Enter a shift value (the alphabet offset)
    The result will be printed
    
    If you choose to decrypt:
        - Select the type of decryption you want, either a specific shift decryption, or run though all options
    If you chose specific:
        - Enter the encrypted message
        - Enter the shift value you wish to decrypt it by
    The result will be printed
    If you chose all:
        - Enter the encrypted message
        - The program will run though all options, select which one looks correct or type 0 if none of them look correct.
    The results will be printed
    
    Please note that anything that are not standard letters may give unexpected results.
    
    ''')

def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please type a valid response ")
        else:
            return response

def not_blank_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            if user_input.isdigit():  # Check if the input is a valid integer
                return int(user_input)  # Convert the input to an integer
            else:
                print("Please enter a valid integer.")
        else:
            print("Input cannot be blank.")

def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print("Please enter a valid response")

def encrypt(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]

        if char==" ":
            result+=" "

        elif (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt_all(message):
    for key in range (len(letters)):
        translated = ''
        for ch in message:
            if ch in letters:
                num = letters.find(ch)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + ch
        print('With shift of %s: %s' % (key, translated))

# main

# vars
yes_no_list = ["yes", "no"]
option_list = ["encrypt", "decrypt"]
decryption_list = ["specific", "all"]
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

all_type = []
all_pre_message = []
all_shift = []
all_post_message = []

cipher_dict = {
    "Type": all_type,
    "Pre message": all_pre_message,
    "Shift": all_shift,
    "Post message": all_post_message
}

cipher_frame = pandas.DataFrame(cipher_dict)

want_instructions = string_checker("Do you want to read the instructions? ", 1, yes_no_list)

if want_instructions == "yes":
    instructions()

while True:

    option = string_checker("Do you wish to encrypt or decrypt a message? ", 1, option_list)

    if option == 'encrypt':

        type = "encryption"

        get_pre_message = not_blank("Please enter the message you wish to encrypt. ")

        get_message = get_pre_message.upper()

        get_shift = not_blank_int("Please enter the desired shift value. ")

        output = encrypt(get_message, get_shift)

    elif option == 'decrypt':

        type = "decryption"

        decryption_method = string_checker("Would you like to input a specific shift value, or run though all possible combinations?\n (please write specific/all) ", 1, decryption_list)

        if decryption_method == "specific":

            get_pre_message = not_blank("Please enter the message you wish to decrypt. ")

            get_message = get_pre_message.upper()

            get_shift = not_blank_int("Please enter a shift value. -")

            get_shift = -abs(get_shift)

            output = encrypt(get_message, get_shift)

        elif decryption_method == "all":

            get_pre_message = not_blank("Please enter the message you wish to decrypt ")

            get_message = get_pre_message.upper()

            decrypt_all(get_message)

            get_shift = not_blank_int("Which shift value gave the correct decryption? (Put 0 for none) ")

            get_shift = -abs(get_shift)

            output = encrypt(get_message, get_shift)

    print()
    print("***** RESULT *****")
    print()
    if get_shift == -0 and type == "decryption":
        print("There was no correct decryption found.")
    else:
        print("The {} result is: {}".format(type, output))

    all_type.append(type)
    all_pre_message.append(get_message)
    all_shift.append(get_shift)
    all_post_message.append(output)

    cipher_frame = pandas.DataFrame(cipher_dict)


    loop = string_checker("Would you like to continue? ", 1, yes_no_list)

    if loop == "yes":

        continue

    elif loop == "no":

        print("***** ALL RESULTS *****")
        print()
        print(cipher_frame)

        break






