# need this only to expect name
from use_test import megamain
def __init__():

    def search_str(file_path, word):
        with open(file_path, 'r') as file:
            # read all content of a file
            content = file.read()
            # check if string present in a file
            if word in content:
                print('string exist in a file')
                with open('readme.txt', 'r') as fp:

                    lines = fp.readlines()
                    for line in lines:
                        if line.find(word) != -1:
                            print(word, 'string exists in file')
                            print('Line Number:', lines.index(line))
                            print('Line:', line)
                            quit()
                            
                            
            else:
                print('string does not exist in a file')
                quit()
                



    search_str('readme.txt', input('Enter a string to search: '))
    def new_func():
        return megamain()

    new_func()

__init__()
