import pyperclip as pc
import re

text = pc.paste()
text_lines = text.split("\n")
output = []

for line in text_lines:
    # line.split('(')
    if line.startswith("void"):
        args = re.search(r"\((.*?)\)", line)
        if args.group(1) != "":
            line = line.replace('(' + args.group(1) + ')', "(...)")
        line = line.replace('void', '#define')
        line = line.replace(";", "")
        output.append(line)


print(output)


string = ""
for line in output:
    string += line + "\n"

pc.copy(string)

# text = "void test(int i);"
# text = text.split('(')
# print(text)
# prefix = text[0]
# split_pointer = prefix.split('*')
# return_pointer = 0
# if len(split_pointer) != 1:
#     return_pointer = 1
#     print('return pointer')
