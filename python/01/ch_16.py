""""Write a script that prompts the user for:

A file_name where it should write the content.
The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.
After the user enters an empty line, write all of the lines to the file and end the script."


"""

file_name = input("Please enter a file name where you want to write your diary....  ") or "./testing.txt"
print ("Your diary will be created in {0}".format(file_name))
file_name = "../" + file_name
content = []
while True:
    line = input("Please enter a line of text or hit the Enter key without entering any text to exit...")
    if line:
        content.append(line + "\n")
    else:
        break

with open(file_name, mode='w') as f:
    f.writelines(content)
        
