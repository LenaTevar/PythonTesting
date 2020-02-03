

def getLines():
    with open('ReadFile/Files/example.java', 'r') as file_object:
        lines = file_object.readlines()
        print('Reading file')
        return lines


my_lines = getLines()
print(my_lines)
