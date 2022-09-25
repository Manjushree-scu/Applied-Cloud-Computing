import re

file1 = open('company.txt', 'r')
Lines = file1.readlines()
line = Lines[1]

x = re.search(r"\w+\s\w+", line)

file2 = open("company.txt", "w")
file2.write(x.group())
file2.close()
print("Printing File content")
f = open("company.txt", "r")
print(f.read())
