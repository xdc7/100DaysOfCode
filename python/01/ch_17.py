"""Write a script that does the following:

Receives a file_name and line_number as command line parameters.
Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.
Make sure that you handle the following error cases by presenting the user with a useful message:

The file doesn’t exist.
The file doesn’t contain the line_number specified (file is too short)."""


# Prompt user to enter filename and line number as command line params

import argparse, sys

parser = argparse.ArgumentParser(description="Provide a filename and line number to be printed from the same file")
parser.add_argument("filename", help="The file to be read")
parser.add_argument("line_num", help="The line from the file to be printed")

args = parser.parse_args()
is_line_num_found = False
try:
    with open(args.filename) as f:
        for i, line in enumerate(f):
            try:
                if i == int(args.line_num) - 1:
                    print(line)
                    is_line_num_found = True
                    break
            except ValueError:
                print ("Invalid Line number!")
                break    
except IOError as err:
    print ("File not found!")
    sys.exit()
except NameError as err:
    print ("File not found!")
    sys.exit()


if not is_line_num_found:
    print ("Line not found!")
    

