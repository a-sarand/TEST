import os

filename= input("File name:\n")

if os.path.exists(filename):
    print(True)
else:
    print(False)

