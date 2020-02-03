from pathlib import Path


def recursiveJavaSearch(folder):
    pathlist = Path(folder).glob('**/*.java')
    for path in pathlist:
        path_in_str = str(path)
        print('>'+path_in_str)
        getLines(path_in_str)

    return


def getLines(path):
    with open(path, 'r') as file_object:
        lines = file_object.readlines()
        print('Reading. File len: ', len(lines))
    return lines


recursiveJavaSearch('ReadFile/Files')
