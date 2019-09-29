# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 28 April 2018
# Last Modified Date: 2 May 2018
# This code is the main code where all the functions to decode the morse code
# sequence using main() function and to analyse it will be called


from decoder_29325013 import Decoder
from character_29325013 import CharacterAnalyser
from word_29325013 import WordAnalyser
from sentence_29325013 import SentenceAnalyser


def morse_code_decoder():
    continue_exit = 'Y'
    morse_code = Decoder()  # object of class type Decoder
    decoded_sequences = []  # contains all decoded morse code sequences
    print(morse_code)
    while continue_exit in ('Y', 'y'):
        # this loop will let the user input the morse code sequences until he
        #  wants to
        morse_input = input(
            "Please enter the morse code sequence you want to decode:")
        decoded_value = morse_code.decode(morse_input)

        if decoded_value == "Invalid_length":
            # if the input is of invalid length it will be rejected
            print(morse_input, " is not of correct length. Please enter again")
            continue_exit = 'Y'

        elif decoded_value == "Incorrect_combination":
            # if the input is of invalid characters it will be rejected
            print(morse_input,
                  " is not a combination of 1, 0, *. Please enter again")
            continue_exit = 'Y'

        elif decoded_value == "Invalid_morse_Code":
            # if input consists of invalid morse code values it will be rejected
            print(morse_input, " is invalid Morse Code")
            continue_exit = 'Y'

        elif decoded_value == "No_punctuation":
            # if input does not contains punctuation at end it will be rejected
            print(morse_input,
                  "does not end with a punctuation, Please enter again")
            continue_exit = 'Y'

        elif decoded_value == "Incorrect_punctuation":
            # if input contains 2 punctuation marks together it will be rejected
            print(morse_input, "does not have correct set of punctuation in it,"
                               " Please enter again")
            continue_exit = 'Y'

        elif decoded_value == "No_triple_asterisks":
            # if the input does not contain atleast one *** it will be rejected
            print(morse_input,
                  "does not have atleast one set of ***, Please enter again")
            continue_exit = 'Y'

        elif decoded_value == "Incorrect_spaces":
            # if the input contains 2 or more than 3 *'s it will be rejected
            print(morse_input, " has incorrect spaces, Please enter again")

        else:
            # else input will be decoded and all the decoded sequences
            # will be stored as below
            decoded_sequences.append(decoded_value)
            continue_exit = input("Do you want to enter more morse code "
                                  "sequences? Press Y or N")

    return decoded_sequences


# this function will call function from class CharacterAnalyser and analyses
# each character in the decoded morse code sequences and prints it
def character_counter(decoded_sequence):
    character = CharacterAnalyser()  # object of class type CharacterAnalyser
    for each in decoded_sequence:
        character.analyse_characters(each)

    print("The number of each characters in the input sequences is:")
    print(character)


# this function will call function from class WordAnalyser and analyses
# each word in the decoded morse code sequences and prints it
def word_counter(decoded_sequences):
    word = WordAnalyser()  # object of class type WordAnalyser
    for each in decoded_sequences:
        word.analyse_words(each)

    print("The number of each words in the input sequences is:")
    print(word)


# this function will call function from class SentenceAnalyser and analyses
# each type of sentence in the decoded morse code sequences and prints it
def sentence_counter(decoded_sequences):
    sentence = SentenceAnalyser()
    for each in decoded_sequences:
        sentence.analyse_sentences(each)

    print("The type of each sentence in the input sequences is:")
    print(sentence)


# this is the main function that will determine the flow of the invocation
# of each of the above defined functions
def main():
    decoded = morse_code_decoder()
    continue_exit = 'Y'
    print("Now the morse code sequences will be analysed")
    while continue_exit in ('Y', 'y'):
        # this variable will allow the user to keep analysing the input
        # sequences until he wants to stop
        level = input("Please enter the analysis level from the below option:\n"
                      "1. Character level\n"
                      "2. Word level\n"
                      "3. Sentence level\n"
                      "4. All levels")

        if level is None or level == '':
            level = 'None'
        else:
            level = int(level)
        # this will allow user to select the level of analysis he wants to view
        if level == 1:  # character level
            character_counter(decoded)

        elif level == 2:  # word level
            word_counter(decoded)

        elif level == 3:  # sentence level
            sentence_counter(decoded)

        elif level == 4:  # at all the levels
            character_counter(decoded)
            word_counter(decoded)
            sentence_counter(decoded)

        else:  # anything apart from 4 options will be rejected
            print("Invalid Input")

        continue_exit = input("Do you want to analyse more? Press Y or N")


if __name__ == '__main__':

    # invoke main function on execution of the code
    print("Welcome to Morse Code Decoder  !!")
    main()
    print("Thanks for using Morse Code Decoder Analyser !!")
