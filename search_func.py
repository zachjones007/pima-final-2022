
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
        else:
            print('string does not exist in a file')

       

search_str('readme.txt', input('Enter a string to search: '))
