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

