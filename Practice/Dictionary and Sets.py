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
print(student)