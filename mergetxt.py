import fileinput
import glob

file_list = glob.glob("*.txt")

with open('combined.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)