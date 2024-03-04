with open("demo1.txt", "r") as f:
    content = f.read()
    tokens = [content[i:i+5] for i in range(0, len(content), 5)]
    formatted_tokens = "\\".join(tokens)
    print(formatted_tokens)