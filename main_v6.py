# imports
import datetime
import pandas
from datetime import date
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
    
    Please note that special characters may give unexpected results.
    The current supported punctuation is . , ? ! / ( )
    
    ''')
# checks for blank responses


def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please type a valid response ")
        else:
            return response

# checks for numbers (whole)


def not_blank_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            if user_input.isdigit():  # Check if the input is a valid integer
                return int(user_input)  # Convert the input to an integer
            else:
                print("Please enter a valid whole number.")
        else:
            print("Input cannot be blank.")

# checks for valid responses depending on the question asked


def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print("Please enter a valid response")

# encryption function, also works for decryption when given a negative shift


def encrypt(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]

        if char==" ":
            result+=" "
        # if space, ignore it
        elif char.isdigit() or char in [".", ",", "?", "!", "/", "(", ")"]:
            result += char
        # if the character is one of these, ignore it
        elif (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

# decrypt all function


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
        # printing results
        print('With shift of %s: %s' % (key, translated))

# main

# vars
# lists for string checker
yes_no_list = ["yes", "no"]
option_list = ["encrypt", "decrypt"]
decryption_list = ["specific", "all"]

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# pandas variables
all_type = []
all_pre_message = []
all_shift = []
all_post_message = []

# pandas dictionary
cipher_dict = {
    "Type": all_type,
    "Pre message": all_pre_message,
    "Shift": all_shift,
    "Post message": all_post_message
}

# establish table frame
cipher_frame = pandas.DataFrame(cipher_dict)

# start of program
print("Welcome to a Caesar Cipher program")
name = not_blank("What is your name? ")

print("Welcome, {}!".format(name))
want_instructions = string_checker("Do you want to read the instructions? (yes/no) ", 1, yes_no_list)

if want_instructions == "yes":
    instructions()

# begin encrypt/decrypt loop
while True:

    option = string_checker("Do you wish to encrypt or decrypt a message? (encrypt/decrypt) ", 1, option_list)

    # encryption section
    if option == 'encrypt':

        # type variable is important for results table
        type = "encryption"

        get_pre_message = not_blank("Please enter the message you wish to encrypt. ")

        # convert message to upper case
        get_message = get_pre_message.upper()

        get_shift = not_blank_int("Please enter the desired shift value. ")

        # runs the encryption function and sets result to output
        output = encrypt(get_message, get_shift)

    # decryption section
    elif option == 'decrypt':

        type = "decryption"

        decryption_method = string_checker("Would you like to input a specific shift value, or run though all possible combinations? (specific/all) ", 1, decryption_list)

        # specific decryption variant
        if decryption_method == "specific":

            get_pre_message = not_blank("Please enter the message you wish to decrypt. ")

            # converts message to upper case
            get_message = get_pre_message.upper()

            get_shift = not_blank_int("Please enter a shift value. -")

            # converts shift to negative
            get_shift = -abs(get_shift)

            # encryption function, effectively decryption with negative shift
            output = encrypt(get_message, get_shift)

        # all decryption variant
        elif decryption_method == "all":

            get_pre_message = not_blank("Please enter the message you wish to- decrypt ")

            # converts message to upper case
            get_message = get_pre_message.upper()

            # runs decrypt all function
            decrypt_all(get_message)

            get_shift = not_blank_int("Which shift value gave the correct decryption? (Put 0 for none) ")

            # converts shift to negative, only used for results table
            get_shift = -abs(get_shift)

            output = encrypt(get_message, get_shift)

    # single results
    print()
    print("***** RESULT *****")
    print()

    # -0 shift comes from all decryption when a correct result cant be found
    if get_shift == -0 and type == "decryption":
        print("There was no correct decryption found.")
        output = "N/A"
    else:
        print("The {} result is: {}".format(type, output))

    # inserts variables to table
    all_type.append(type)
    all_pre_message.append(get_message)
    all_shift.append(get_shift)
    all_post_message.append(output)

    cipher_frame = pandas.DataFrame(cipher_dict)

    # checks to restart the loop or end
    loop = string_checker("Would you like to continue? ", 1, yes_no_list)

    if loop == "yes":

        # continue loop
        continue

    elif loop == "no":

        # results section
        print("***** ALL RESULTS *****")
        print()
        print(cipher_frame)
        print()

        export = string_checker("Would you like to export the results to a text file? ", 1, yes_no_list)

        if export == "yes":

            today = date.today()
            time = datetime.datetime.now()

            # get system date
            day = today.strftime("%d")
            month = today.strftime("%m")
            year = today.strftime("%Y")

            # get system time
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            second = time.strftime("%S")

            # assign date and time to file name
            filename = "CIPHER_{}_{}_{}_{}_{}.txt".format(year, month, day, hour, minute)


            # convert table to string for export
            cipher_txt = pandas.DataFrame.to_string(cipher_frame)

            text_file = open(filename, "w+")

            # writing information to file
            text_file.write("***** ALL RESULTS *****\nUser: {}\n\n{}".format(name, cipher_txt))
            print()
            # name of file that was created
            print("The results have been exported as {}".format(filename))

        print("Thanks for using the Caesar Cipher program.")

        # end of program
        break






