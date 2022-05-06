import pyperclip as pc
import re
from enum import Enum, auto


class ReturnType(Enum):
    UNKNOWN = 0
    POINTER = auto()
    VOID = auto()
    BOOL = auto()
    NUMBER = auto()

def chg_func_do(text):
    # text = "IN void *test(int i);"
    text = text.split('(')
    # print(text)
    prefix = text[0]
    split_pointer = prefix.split('*')
    return_pointer = 0

    if len(split_pointer) != 1:
        return_pointer = 1
        prefix = ' '.join(split_pointer)
        # print('return pointer')
    # print(prefix)

    split_space = prefix.split(' ')
    func_name = split_space.pop()
    prefix = ' '.join(split_space)
    # print(prefix)
    # print(func_name)

    return_type = ReturnType.UNKNOWN
    number_type = ["u8", "u16", "u32", "u64", "i8",
                "i16", "i32", "i64", "int", "float", "double"]

    if return_pointer != 1:
        if "void" in prefix:
            return_type = ReturnType.VOID
        if "bool" in prefix:
            return_type = ReturnType.BOOL
        if any(type in prefix for type in number_type):
            return_type = ReturnType.NUMBER
    else:
        return_type = ReturnType.POINTER

    # print(return_type)

    postfix = ''
    match return_type:
        case ReturnType.POINTER:
            postfix = "NULL"
        case ReturnType.BOOL:
            postfix = "false"
        case ReturnType.NUMBER:
            postfix = "0"

    prefix = "#define " + func_name + "(...)"
    output = prefix + " " + postfix
    # print(output)
    return output

text = pc.paste()
text_lines = text.split("\n")
output = []

for line in text_lines:
    if len(line) < 3:
        continue
    if line.startswith("//"):
        continue # skip comments
    output.append(chg_func_do(line))

print(output)

string = ""
for line in output:
    string += line + "\n"

pc.copy(string)
