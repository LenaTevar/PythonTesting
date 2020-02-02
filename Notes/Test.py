regex_class = 'class'
with open("PythonTesting/Notes/mytest.java") as myjavafile:
    myjavastr = myjavafile.read()
containsClass = '\nIs class ' + str(regex_class in myjavastr)
whereEndsClass = myjavastr.find(regex_class)
whereEndsNameclass = myjavastr.find(' ', whereEndsClass)
mypartition = myjavastr.partition(regex_class)
print(mypartition)
print(str(whereEndsClass) + ' - ' + str(whereEndsNameclass))
with open("PythonTesting/Notes/myfile.txt", "r+") as mytextfile:
    mytext = mytextfile.read()
    mytextfile.write(mytext)

print('Done')
