with open(r"C:\Users\Donap\Desktop\Lines.txt", 'r+') as file:
    print(file.read())
    lines = file.readlines()

    file_length = len(lines)
    print(file_length)

    new_file = list("")

    for x in range(file_length):
        if x == 4:
            print("No line\n")

        else:
            new_file.append(lines[x])
            file.write(new_file)


