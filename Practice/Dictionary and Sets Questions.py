
# Store word meanings in python dictionary

# word_meanings = {'table' : ['a piece of furniture','list of facts and figures'] , 'cats' : 'a small animal'}
# print(word_meanings.keys())
# print(word_meanings['table'])
# print(word_meanings['cats'])



# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# subjects = {'Python','java','C++','Python','javascript','java','Python','java','C++','C'} 

# print(f'Number of classrooms required is {len(subjects)}.')


# WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = {}

physics = int(input('Enter the marks of Physics : '))
marks.update({'Physics' : physics})

maths = int(input('Enter the marks of Maths : '))
marks.update({'Maths' : maths})

chemistry = int(input('Enter the marks of Chemistry : '))
marks.update({'Chemistry' : chemistry})

print(marks)