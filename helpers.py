import hashlib
def hash(text):
    hash_object = hashlib.sha256()
    hash_object.update(text.encode())
    return(hash_object.hexdigest())
