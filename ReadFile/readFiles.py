import os

directory = os.fsencode('ReadFile/Files')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".java"):
        print('Found!!!!  ' + os.path.join(filename))
        continue
    else:
        print('Uggh:  ' + os.path.join(filename))
        continue
