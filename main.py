# imports

# functions

def instructions():
    print("poo funny")

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
            if user_input.isdigit():
                return int(user_input)
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
    for key in range(len(letters)):
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

want_instructions = string_checker("Do you want to read the instructions? ", 1, yes_no_list)

if want_instructions == "yes":
    instructions()

print()

option = string_checker("Do you wish to encrypt or decrypt a message? ", 1, option_list)

if option == 'encrypt':
    print("You chose to encrypt")

    get_message = not_blank("Please enter the message you wish to encrypt. ")

    get_shift = not_blank_int("Please enter the desired shift value. ")

    output = encrypt(get_message, get_shift)

    print("***** ENCRYPTION RESULT *****")
    print()
    print("The encrypted message is: {}".format(output))

elif option == 'decrypt':
    print("You chose to decrypt")

    decryption_method = string_checker("Would you like to input a specific shift value, or run though all possible combinations?\n (please write specific/all) ", 1, decryption_list)

    if decryption_method == "specific":

        get_message = not_blank("Please enter the message you wish to decrypt. ")

        get_shift = not_blank_int("Please enter a shift value. -")

        get_shift = -abs(get_shift)

        output = encrypt(get_message, get_shift)

        print("***** DECRYPTION RESULT *****")
        print()
        print("The encrypted message is: {}".format(output))

    elif decryption_method == "all":

        get_message = not_blank("Please enter the message you wish to decrypt ")

        print('***** DECRYPTION RESULT *****')
        print()
        decrypt_all(get_message)

