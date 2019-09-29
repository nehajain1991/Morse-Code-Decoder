# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 28 April 2018
# Last Modified Date: 3 May 2018
# This code will be used to decode the input morse code sequence by the user


class Decoder:
    def __init__(self):
        # function to initialise the instance variable fo the class
        self.morse_code_dict = {  # creating a dictionary that stores all the
            # characters and their Morse code values
            'A': '01',
            'B': '1000',
            'C': '1010',
            'D': '100',
            'E': '0',
            'F': '0010',
            'G': '110',
            'H': '0000',
            'I': '00',
            'J': '0111',
            'K': '101',
            'L': '0100',
            'M': '11',
            'N': '10',
            'O': '111',
            'P': '0110',
            'Q': '1101',
            'R': '010',
            'S': '000',
            'T': '1',
            'U': '001',
            'V': '0001',
            'W': '011',
            'X': '1001',
            'Y': '1011',
            'Z': '1100',
            '0': '11111',
            '1': '01111',
            '2': '00111',
            '3': '00011',
            '4': '00001',
            '5': '00000',
            '6': '10000',
            '7': '11000',
            '8': '11100',
            '9': '11110',
            '.': '010101',
            ',': '110011',
            '?': '001100'
        }

    def __str__(self):
        # override function to print the details of an object in a readable
        # format
        print_string = 'The morse code dictionary defined is:' \
                       '\nCharacter         Morse Code\n'
        for key, value in self.morse_code_dict.items():
            print_string += (key + "                  " + value + '\n')

        return print_string

    def get_dict(self):
        # getter of the instance variable of the class
        return self.morse_code_dict

    def set_dict(self, morse_code_dict):
        # setter of the instance variable of the class
        self.morse_code_dict = morse_code_dict

    # this function will check the input if it is valid or not
    def check_input(morse_code_sequence):
        length_input = len(morse_code_sequence)

        if length_input < 1 or morse_code_sequence == "":
            # check the valid length of the input
            # check for the minimum length as 1 in the Morse Code sequence
            return "Invalid_length"

        elif '***' not in morse_code_sequence:
            # check if there is atleast one *** in the sequence
            return "No_triple_asterisks"

        else:  # if the characters entered are combination of 1, 0, *
            for counter in range(length_input):
                # checks if the input is a combination of 1, 0, *
                if morse_code_sequence[counter] not in ("1", "0", "*"):
                    return "Incorrect_combination"

        return 'True'

    # this function will check valid conditions of morse code after decoding
    def check_valid_morse_code(self, morse_code_list):
        space = 0
        morse_code_decode_output = []

        for count in range(0, len(morse_code_list)):
            if morse_code_list[count] not in self.morse_code_dict.values() \
                    and morse_code_list[count] != "":
                # if Morse code sequence value is not present in the Dictionary,
                # the morse code will be rejected
                return "Invalid_morse_Code"

            elif morse_code_list[count] == "" and \
                    morse_code_list[count + 1] == "":
                # this will check the number of * present, if they are more
                # than 3, morse code will be rejected
                if space == 0:
                    morse_code_decode_output.append(' ')
                    space = 1

                else:
                    return "Incorrect_spaces"
                count += 1

            elif (morse_code_list[count] == "" and morse_code_list[
                count + 1] in self.morse_code_dict.values()
                  and morse_code_list[
                      count - 1] in self.morse_code_dict.values()) or \
                    morse_code_list[len(morse_code_list) - 1] == "":
                # this will count if there are 2 stars in the input, i
                # t will be rejected
                return "Incorrect_spaces"

            else:
                # if all above are true, the input will be decoded
                for key, value in self.morse_code_dict.items():
                    if morse_code_list[count] == value:
                        morse_code_decode_output.append(key)
                        space = 0

        for count in range(len(morse_code_decode_output)):
            # the decoded morse code will be checked for punctuation at end
            if morse_code_decode_output[len(morse_code_decode_output) - 1] \
                    not in (',', '.', '?'):
                return "No_punctuation"

            # the decoded morse code will be checked for punctuation at start
            # and that no 2 punctuations occur together
            elif count != len(morse_code_decode_output) - 1:
                if ((morse_code_decode_output[count] in (',', '.', '?')
                     and (morse_code_decode_output[count + 1] in
                          (',', '.', '?')))
                        or (morse_code_decode_output[count] in (',', '.', '?')
                            and morse_code_decode_output[count + 1] == ' '
                            and (morse_code_decode_output[count + 2] in
                                 (',', '.', '?')))
                        or morse_code_decode_output[0] in (',', '.', '?')):
                    return "Incorrect_punctuation"

        return morse_code_decode_output

    def decode(self, morse_code_sequence):
        # function to analyse the number of words in the morse sequence
        valid_input = Decoder.check_input(morse_code_sequence)
        # input is checked for validity

        if valid_input == 'True':
            # splits the input for them to decode
            morse_code_list = morse_code_sequence.split("*")

            # the input is checked for the conditions
            valid_morse_code = self.check_valid_morse_code(morse_code_list)
            if valid_morse_code in (
                    "Incorrect_punctuation", "No_punctuation",
                    "Incorrect_spaces",
                    "Invalid_morse_Code"):
                return valid_morse_code
            else:
                # if conditions are true, the decoded value will be printed
                morse_code_decode_out = "".join(valid_morse_code)

            print("The decoded value of", morse_code_sequence, "is",
                  morse_code_decode_out)

        else:
            return valid_input

        return morse_code_decode_out
