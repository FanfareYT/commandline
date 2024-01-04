import sys

print("Hello! usn: fanfare, pwd: 1234")

while True:
    _this = sys.modules[__name__]
    for _n in dir():
        if _n[0]!='_': 
            delattr(_this, _n)
    import sys
    from CLib import *
    loginLoop = True
    while loginLoop:
        usn = ""
        pwd = ""
        usn = input("USERNAME: ")
        pwd = hasher(input("PASSWORD: "))
        log(f"New login attempt with username '{usn}'.")
        
        params = userParams(usn)
        cpass = params[0]
        rank = params[1]
        
        if cpass == "Null":
            log("Invalid password format at user " + usn, 'e')
        else:
            if cpass == pwd:
                login = True
                loginLoop = False
            else:
                login = False
                log(f"Failed login attempt with username {usn}.")
                print("Incorrect username or password.")
    
    log("Successful login attempt.")
     
    cmdLoop = True
    user = usn
    while cmdLoop:
        cmdinp = input(f"@{user}$>>> ")
        if cmdinp == "":
            cmdinp = "Null Null"
        cmd = cmdinp.split(" ")
        command = cmd[0]
        try:
            parameters = cmd[1:]
        except:
            pass
            
        if command == "su":
            if rank > 2 and userExists(cmd[1]):
                user = cmd[1]
            else:
                log("Insufficiant rank or that user doesn't exist.", "d")
            
        elif command == "cu":
            if rank > 2:
                try:
                    newUSN = cmd[1]
                    newPWD = hasher(cmd[2])
                except IndexError:
                    print("Invalid cu format. Use 'cu <username> <password>' and try again.")
                try:
                    newRANK = cmd[3]
                except IndexError:
                    newRANK = 1
                        
                if not userExists(cmd[1]):
                    remove_last_line("users.txt")
                    f = open("users.txt", "a")
                    f.write("#" + newUSN)
                    f.write("\npwd:" + newPWD)
                    f.write("\nrank:" + str(newRANK))
                    f.write("\n#end")
                    f.close()
                else:
                    log(f"System to create user '{cmd[1]}', but user already exists!", "w")
            else:
                log("Insufficiant rank.", "d")
            
        elif command == "logout":
            user = "none"
            break
            
        elif command == "stop":
            endprog("s")
        
        else:
            try:
                if cmd[1] == "-h":
                    try:
                        sys.path.append('commands')
                        command_module = __import__(command)
                        execute_command = getattr(command_module, 'get_help')
                        result = execute_command(parameters)
                        sys.path.pop()
                        print(result)
                        log(f""""{cmdinp}" was executed.""")
                    except ImportError:
                        log(f""""{command}.py" was not found.""", "w")
                    except AttributeError:
                        log(f""""{command}.py" is not formatted correctly. Missing "get_help(parameters)" function." """, "e")
                        
                elif cmd[1] == "-a":
                    try:
                        sys.path.append('commands')
                        command_module = __import__(command)
                        execute_command = getattr(command_module, 'get_about')
                        result = execute_command(parameters)
                        sys.path.pop()
                        print(result)
                        log(f""""{cmdinp}" was executed.""")
                    except ImportError:
                        log(f""""{command}.py" was not found.""", "w")
                    except AttributeError:
                        log(f""""{command}.py" is not formatted correctly. Missing "get_about(parameters)" function." """, "e")
                        
                else:
                    try:
                        sys.path.append('commands')
                        command_module = __import__(command)
                        execute_command = getattr(command_module, 'execute_command')
                        result = execute_command(parameters)
                        sys.path.pop()
                        print(result)
                        log(f""""{cmdinp}" was executed.""")
                    except ImportError:
                        log(f""""{command}.py" was not found.""", "w")
                    except AttributeError:
                        log(f""""{command}.py" is not formatted correctly. Missing "execute_command(parameters)" function." """, "e")
            except IndexError:
                log("Invalid parameters. Try using a -n?", "w")