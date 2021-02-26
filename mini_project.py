'''
Description of the code:- This code is used to search the words asked by the
user and based on the number of keywords entered, a separate 'keyword.txt' file
is created where the keyword and its adjacent words are written in new line for
each word in respective files. In case of entered keyword not available in the
file it displays appropriate error message for that.

Author: Mohammed Ijaz
Contact: mohammed.ijaz@ltts.com
Date of creation: 22/02/2021

'''


import re

import os


class Classfirst:

    def __init__(self):  # user input for no of search operation
        self.flag = True
        # number of words searched
        self.nos = input("Enter the number of keyword you want to search:\n")
        # Read only integer input from user else keep reading
        while self.flag:
            if self.nos.isdigit():
                self.flag = False
            else:
                print("Please enter the correct input value")
                self.nos = input("Enter the number of keyword to search: \n")


class Searchclass(Classfirst):  # class to perform search operation

    def function_search_writefile(self):

        for _ in range(int(self.nos)):

            smt = ''

            count = 0

            Search_key = input("Enter Search Key\n")    # read keyword

            file_name = Search_key + '.txt'

            write_file = open(file_name, 'w')

            read_file = open("Input.txt", 'r')  # open file in write mode

            read_file1 = read_file.readlines()

            for line in read_file1:  # append each line of text file to string
                smt += line

            # removing special characters and new lines from string
            smt = re.sub(r'\W+', ' ', smt)

            newstr = smt.split(' ')
            # itterating through out the string and searching for keyword
            for x in range(len(newstr)):

                if newstr[x].lower() == Search_key.lower():
                    write_file.write(newstr[x - 1] + ' ' + newstr[x] +
                                     ' ' + newstr[x + 1] + '\n')

                    count += 1

            if count != 0:  # If no word was found print message
                write_file.write('Total count of ' + Search_key +
                                 ' in input file is ' + str(count))

            write_file.close()

            # if no word was found delete empty file created previously
            if count == 0:

                print("Keyword not found in the file\n")

                if os.path.isfile(file_name):
                    os.remove(file_name)

            write_file.close()

            read_file.close()
clas_object = Searchclass()

clas_object.function_search_writefile()
