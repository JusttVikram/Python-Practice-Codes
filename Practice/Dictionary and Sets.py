                                                        # DICTIONARY

info = {
    "course name" : "Python",
    "Topics" : ("List and Tuples", "Dictionary and Sets"),
    "Duration" : 120,
    "is_mandatory" : True

    }

# Nested dictionary

student = {
    "name" : "Vikram",
    "Subjects" : {
        "Physics" : 99,
        "Chemistry" : 99,
        "Maths" : 100
    }
}


print(student["Subjects"])
print(student["Subjects"]["Physics"])
print(student["Subjects"]["Chemistry"])
print(student["Subjects"]["Maths"])
print(student["name"])

print(student.keys())
print(student.values())
print(student.items())


print(student.get("name"))
student.update({"City" : "Delhi"})
print(student["City"])

new_dict = {'Gender' : 'Male'}
student.update(new_dict)
print(student)

                                                                # SETS

set_A = set()

set_A.add(44)
set_A.add(4)
set_A.add(14)
set_A.add(64)
set_A.add(84)


set_A.remove(4)
set_A.add(4)
set_A.pop()
print(set_A)
set_A.clear()
print(set_A)


set1= {1,2,3,5,6}
set2 = {4,5,6,7,8,9,0}

print(set1.union(set2))
print(set1.intersection(set2))
