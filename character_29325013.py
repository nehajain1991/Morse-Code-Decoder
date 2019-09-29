# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 28 April 2018
# Last Modified Date: 3 May 2018
# This code will analyse the number of characters given as the input by the user
# in individual morse code sequence and the entire morse code sequence


class CharacterAnalyser:
    def __init__(self):
        # function to initialise the instance variable fo the class
        self.count_character_dictionary = {}

    def __str__(self):
        # override function to print the details of an object in a readable
        # format
        print_string = ''
        for key, value in self.count_character_dictionary.items():
            if value != 0:
                print_string += (key + " : " + str(value) + "\n")
        return print_string

    def get_dict(self):
        # getter of the instance variable of the class
        return self.count_character_dictionary

    def set_dict(self, count_character_dictionary):
        # setter of the instance variable of the class
        self.count_character_dictionary = count_character_dictionary

    def analyse_characters(self, decoded_sequence):
        # function to analyse the number of words in the morse sequence
        count_individual = {}  # dictionary to analyse the character in
        # individual morse code sequence
        for morse_code_character in decoded_sequence:
            for morse_code_alphabets in morse_code_character:
                if morse_code_alphabets not in (" ", "", ",", ".", "?"):
                    # store the character count in all morse code sequences
                    if morse_code_alphabets in \
                            self.count_character_dictionary.keys():
                        self.count_character_dictionary[
                            morse_code_alphabets] += 1

                    else:
                        self.count_character_dictionary[
                            morse_code_alphabets] = 1

                    # store character count in individual morse code sequences
                    if morse_code_alphabets in count_individual.keys():
                        count_individual[morse_code_alphabets] += 1

                    else:
                        count_individual[morse_code_alphabets] = 1

        print("The occurrence of each character in", decoded_sequence, "is:")
        for key, value in count_individual.items():
            print(key, ":", value)
