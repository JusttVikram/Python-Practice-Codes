"""Readind a file."""

# f = open("Sample.txt", "r")
# data = f.read()      #reads entire file.
# # data1 = f.readline()  #reads one line at a time.
# print(data)
# print(type(data))
# f.close()

"""Writing a file."""

# f = open("Sample.txt", "w")  #Overrites the entire file.
f = open("Sample.txt", "a")    #adds to the file.
f.write("Yeh hai naya content.\n")
f.close()
