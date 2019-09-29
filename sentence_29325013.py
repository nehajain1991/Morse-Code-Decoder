# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 28 April 2018
# Last Modified Date: 3 May 2018
# This code will analyse the number of type of sentences given as the input by
# the user in individual morse code sequence and the entire morse code sequence


class SentenceAnalyser:
    def __init__(self):
        # function to initialise the instance variable fo the class
        self.count_sentence_dictionary = {
            'Question': 0,
            'Clause': 0,
            'Sentence': 0
        }

    def __str__(self):
        # override function to print the details of an object in a readable
        # format
        print_string = ''
        for key, value in self.count_sentence_dictionary.items():
            if value != 0:
                print_string += ('Number of ' + key + " : " + str(value) + "\n")
        return print_string

    def get_dict(self):
        # getter of the instance variable of the class
        return self.count_sentence_dictionary

    def set_dict(self, count_sentence_dictionary):
        # setter of the instance variable of the class
        self.count_sentence_dictionary = count_sentence_dictionary

    def analyse_sentences(self, decoded_sequence):
        # function to analyse the number of words in the morse sequence
        count_individual = {}  # dictionary to analyse the sentence type in
        # individual morse code sequence
        for each in decoded_sequence:
            if each in (',', '.', '?'):
                # changing each punctuation type to dictionary key
                if each == '?':
                    each = 'Question'
                elif each == '.':
                    each = 'Sentence'
                else:
                    each = 'Clause'

                # store the sentence count in all morse code sequences
                if each not in self.count_sentence_dictionary.keys():
                    self.count_sentence_dictionary[each] = 1

                else:
                    self.count_sentence_dictionary[each] += 1

                # store the sentence count in each morse code sequences
                if each not in count_individual.keys():
                    count_individual[each] = 1

                else:
                    count_individual[each] += 1

        # to correct the count for Clause type of sentence
        if 'Clause' in count_individual.keys() and \
                ',' != decoded_sequence[len(decoded_sequence)-1]:
            self.count_sentence_dictionary['Clause'] += 1
            count_individual['Clause'] += 1

        print("The occurrence of each sentence in", decoded_sequence, "is:")
        for key, value in count_individual.items():
            print("Number of", key, ":", value)
