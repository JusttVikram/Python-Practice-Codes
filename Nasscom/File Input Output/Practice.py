def write_practice_text_file():
    with open("practice.txt","w") as f:
        f.write("Hi everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java.");

def replace_words():
    with open("practice.txt","r") as f:
        data = f.read()
        new_data = data.replace("Java","Python")
        print(new_data);
    with open("practice.txt", "w")as f:
        f.write(new_data);

def check_words():
    with open("practice.txt","r") as f:
        data = f.read()
        print(data.__contains__("learning"))
        print(data.__contains__("Java"))

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print (line_no)
            line_no+=1
    return -1


check_for_line()