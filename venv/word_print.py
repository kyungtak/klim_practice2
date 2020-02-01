import webbrowser

# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
file1 = open("MyFile.txt","w")

file1.write("Hello \n")
file1.writelines(["This is Kyungtak \n", "This is Marie \n"])

filepath = "Myfile.txt"
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1

    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1


# In order to open text file in notepad, use this function
#webbrowser.open("MyFile.txt")





