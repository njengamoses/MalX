def save_report(filename, content):
    with open(filename, "a") as file:
        file.write(content + "\n")
