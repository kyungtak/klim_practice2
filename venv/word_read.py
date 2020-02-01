import os.path

fname = "Myfile.txt"
if os.path.isfile(fname):
    print("True")
else:
    print("False")

word = input("Which word do you want to write?")
meaning = input("What does mean this word?")



print(word)
print(meaning)
;