import re

import os


class Classfirst:

    def __init__(self):  # user input for no of search operation
        self.flag = True
        self.nos = input("Enter the number of keyword you want to search:\n")
        while self.flag:
            if self.nos.isdigit():
                self.flag = False
            else:
                print("Please enter the correct input value")
                self.nos = input("Enter the number of keyword you want to
                                 search: \n")


class Searchclass(Classfirst):  # class to perform search operation

    def function_search_writefile(self):

        for _ in range(int(self.nos)):

            smt = ''

            count = 0

            Search_key = input("Enter Search Key\n")

            file_name = Search_key + '.txt'

            write_file = open(file_name, 'w')

            read_file = open("Input.txt", 'r')

            read_file1 = read_file.readlines()

            for line in read_file1:
                smt += line

            smt = re.sub(r'\W+', ' ', smt)

            newstr = smt.split(' ')

            for x in range(len(newstr)):

                if newstr[x].lower() == Search_key.lower():
                    write_file.write(newstr[x - 1] + ' ' + newstr[x] +
                                     ' ' + newstr[x + 1] + '\n')

                    count += 1

            if count != 0:
                write_file.write('Total count of ' + Search_key +
                                 ' in input file is ' + str(count))

            write_file.close()

            if count == 0:

                print("Keyword not found in the file\n")

                if os.path.isfile(file_name):
                    os.remove(file_name)

            write_file.close()

            read_file.close()
clas_object = Searchclass()

clas_object.function_search_writefile()
