import hashlib
import re

def hash(text):
    hash_object = hashlib.sha256()
    hash_object.update(text.encode())
    return(hash_object.hexdigest())


def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True

    return False

def check_Gcode(code):
    if len(code) != 10:
        return False
    same_digits = True
    for i in code:
        if i != code[0]:
            same_digits = False
            break
    if same_digits:
        return False
    
    a = int(code[9])
    b = 0
    for i in range(0, 9): 
        b += int(code[i]) * (10 - i)

    b = b % 11
    if ((b >= 2 and a == 11 - b) or (b < 2 and a == b)):
        return True
    return False


print(check_Gcode("1364518473"))
