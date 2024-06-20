readFile = open("sample.txt", "a")
readFile.write("\nThis is a new line injected by python")
readFile.close()

newFile = open("newFile.py", "w")
newFile.write('print("This is a new file made with python")')
