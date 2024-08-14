#   pyimproved - python improved functions
import os, sys



#   binput (better input)
def binput(text="> ", old_input="", handler=None, default=None) -> str:
    if handler == None:
        new_input = input(text)

        if default != None and new_input == "":
            return default
        return new_input

    valid = handler(old_input)
    while not valid:
        new_input = input(text)
        if new_input == "exit": 
            print("[!] Exiting script as requested...")
            sys.exit()

        if default != None and new_input == "":
            return default

        valid = handler(new_input)
        if not valid: print(f"[!] Invalid input \" {repr(new_input)} \"")
        old_input = new_input

    return old_input


#   isYON (is yes or no)
def isYON(value):
    return value.lower() in ['y', 'ye', 'ya', 'yes', 'yay', 'n', 'no', 'na', 'nay']


#   isFile (is valid file path)
def isFile(path):
    return os.path.isfile(os.path.expanduser(path))


#   isDir (is valid directory path)
def isDir(path):
    return os.path.isdir(os.path.expanduser(path))


#   isInt (is integer alse checks strings)
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


#   repeat (repeats the given value n times)
def repeat(value, n):
    return f"{value}"*n


#   isYes (returns true if value is yes)
def isYes(value):
    return value.lower() in ['y', 'ye', 'ya', 'yes', 'yay', 'yessir', 'yuh', 'yuhuh', 'yuh uh', 'mhm']


#   isNo (returns true if value is no)
def isNo(value):
    return value.lower() in ['n', 'no', 'na', 'nuh', 'nay', 'nuhuh', 'nuh uh', 'nope', 'mhm']


#   boxed (puts the gives string in a box)
def boxed(tobox:str, min_width=5, max_width=2**16, print_=True) -> str:
    boxed = list()
    lines = tobox.split('\n')

    if max_width < min_width: max_width = min_width

    longest = len(max(lines, key=len))
    if longest-min_width < 0: longest = min_width
    if longest-max_width > 0: longest = max_width

    lines = [f"│ {line} {repeat(' ', (longest-len(line)))}│" for line in lines]

    longest = len(max(lines, key=len))
    if longest-min_width < 0: longest = min_width
    lines = [f"{line[:max_width-2]} │" for line in lines] if longest - max_width > 0 else lines
    if longest-max_width > 0: longest = max_width

    boxed.append(f"╭{repeat('─', longest-2)}╮")
    for line in lines:
        boxed.append(line)
    boxed.append(f"╰{repeat('─', longest-2)}╯")

    result = '\n'.join(boxed)
    if not print_: return result
    print(result)


#   dprint (dictionary print, to print the dict given prettier)
def dprint(dictionary, print_=True):
    lines = []

    longest = len(max(dictionary.keys(), key=len))
    for k, v in dictionary.items():
        k = f"{k}{repeat('.', longest-len(k))}"
        lines.append(f"{k}.:   {v}")

    result_str = "\n".join(lines)

    if not print_: return result_str
    print(result_str)