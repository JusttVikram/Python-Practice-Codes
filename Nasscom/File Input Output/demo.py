f = open("love.txt", "w")
f.write("I love coding!")
f.close()

f = open("fruits.txt", "w")
fruits = ["apple", "banana", "orange"]
f.writelines(fruits)
f.close()