import re

file1 = open('company.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    x = re.search(r"\w+\sINC", line)
    if x!=None:
        break
    count+=1

if x != None :
    file2 = open("company.txt", "w")
    file2.write(x.group())
    file2.close()
    print("Printing File content")
    f = open("company.txt", "r")
    print(f.read())
else:
    print("No Company name found")
