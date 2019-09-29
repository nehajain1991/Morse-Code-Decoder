# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 28 April 2018
# Last Modified Date: 3 May 2018
# This code will analyse the number of words given as the input by the user in
# individual morse code sequence and the entire morse code sequence


class WordAnalyser:

    def __init__(self):
        # function to initialise the instance variable fo the class
        self.count_word_dictionary = {}

    def __str__(self):
        # override function to print the details of an object in a readable
        # format
        print_string = ''
        for key, value in self.count_word_dictionary.items():
            if value != 0:
                print_string += (key + " : " + str(value) + "\n")
        return print_string

    def get_dict(self):
        # getter of the instance variable of the class
        return self.count_word_dictionary

    def set_dict(self, count_word_dictionary):
        # setter of the instance variable of the class
        self.count_word_dictionary = count_word_dictionary

    def analyse_words(self, decoded_sequence):
        # function to analyse the number of words in the morse sequence
        decoded_sequence_list = decoded_sequence.split(' ')
        # split the morse code sequence to check the number of words in sequence
        count_individual = {}  # dictionary to analyse the words in individual
        # morse code sequence

        for each in decoded_sequence_list:
            if each not in (',', '.', '?'):
                # strip the punctuation mark in case there is no space between
                # the word and punctuation
                each = each.strip(',')
                each = each.strip('.')
                each = each.strip('?')
                # store the word count in all morse code sequences
                if each in self.count_word_dictionary.keys():
                    self.count_word_dictionary[each] += 1
                else:
                    self.count_word_dictionary[each] = 1

                # store the word count in individual morse code sequences
                if each not in count_individual.keys():
                    count_individual[each] = 1

                else:
                    count_individual[each] += 1

        print("The occurrence of each word in", decoded_sequence, "is:")
        for key, value in count_individual.items():
            print(key, ":", value)
