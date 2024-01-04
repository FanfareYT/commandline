def hasher(hash_input):
    output = 0
    last_char = 1
    byte_integers = [ord(char) for char in hash_input]
    for cur_char in byte_integers:
        output += cur_char * cur_char * last_char
        last_char = cur_char
    
    return str(output)

def endprog(status = ""):
    import sys
    if status == "e":
        status_ex = 2
    elif status == "s":
        status_ex = 0
    else:
        status = 1
    sys.exit(status_ex)

def log(msg, typ="i", show=False, file="log.txt"):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    from datetime import datetime
    import time

    if typ == "i":
        color = RESET
        pre = "INFO"
    elif typ == "d":
        color = BLUE
        pre = "DEBUG"
        show = True
    elif typ == "e":
        color = RED
        show = True
        pre = "ERROR"
    elif typ == "w":
        color = YELLOW
        show = True
        pre = "WARN"
    elif typ == "o":
        color = GREEN
        show = True
        pre = "OK"
    
    timestamp = datetime.today()
    
    log = open(file, "a")
    log.write("[ " + str(timestamp) + " ] " + pre + ": " + msg + "\n")
    log.flush()
    log.close()
    
    if show:
        print("[ " + pre + " ] " + color + msg + f"{RESET}\n")

def remove_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if lines:
        lines = lines[:-1]
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print("File is empty.")
        
def userExists(user, file="users.txt"):
    n = open(file)
    lines = n.readlines()
    n.close()
    userExist = False
    for line in lines:
        if line.startswith("#") and line.strip("#").strip("\n") == user:
            userExist = True
        else:
            pass
    return userExist
    
def userParams(usn, file="users.txt"):
    cpass = "Null"
    rank = -1
    if userExists(usn):
        users = open(file, "r")
        userf = users.readlines()
        users.close()
        
        paras = []
        userline = 0
        foundUser = False
        for line in userf:
            if line.startswith("#")and line.strip("#").strip("\n") == usn:
                currentUserLine = userline
                foundUser = True
            
            elif foundUser and line.startswith("#"):
               nextUserLine = userline 
               
            userline += 1
        for num, line in enumerate(userf):
            if num < nextUserLine and num > currentUserLine:
                paras.append(line.strip("\n"))
        
        cpass = "Null"
        for p in paras:
            if p.startswith("pwd:"):
                cpass = p.strip("pwd:")
            elif p.startswith("rank:"):
                rank = int(p.strip("rank:").strip("\n"))
        
    return [cpass, rank]
    
def replace_letters(input_text):
    result = ""
    for letter in input_text:
        if letter.lower() == 'b':
            result += ':b:'
        elif letter.lower() == 'i':
            result += '1'
        elif letter.lower() == 'e':
            result += '3'
        elif letter.lower() == 'a':
            result += '4'
        elif letter.lower() == 'o':
            result += '0'
        elif letter.lower() == 't':
            result += '7'
        else:
            result += letter
    return result    
    
def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found!"

def save_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            return "File saved successfully!"
    except:
        return "Error saving file!"