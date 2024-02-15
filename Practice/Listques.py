#WAP to ask the user to enter names of their 3 favourite movies and store them in a list.


Movies = []
movie1 = input("Enter the name of First movie : ")
movie2 = input("Enter the name of Second movie : ")
movie3 = input("Enter the name of Third movie : ")


Movies.append(movie1)
Movies.append(movie2)
Movies.append(movie3)

print(Movies)


# WAP to check if a list contains a palindrome of elements. (Use copy() method)

list1= [1,2,1]

list1_copy= list1.copy()
list1_copy.reverse()

if list1_copy==list1:
    print("Palindrome exists.")
else:
    print("Palindrome doesn't exists.")