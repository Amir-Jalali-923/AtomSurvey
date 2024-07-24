import hashlib
import re
import csv


# Function to hash a given text using SHA-256
def hash(text):
    hash_object = hashlib.sha256()  # Create a new sha256 hash object
    hash_object.update(text.encode())  # Encode the text to bytes and update the hash object
    return(hash_object.hexdigest())  # Return the hexadecimal digest of the hash

# Function to validate an email address using regex
def check_email(email):
    # Regular expression for validating an email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # Check if the email matches the regex pattern
    if(re.fullmatch(regex, email)):
        return True
    return False

# Function to validate a Gcode
def check_Gcode(code):
    # Gcode must be exactly 10 characters long
    if len(code) != 10:
        return False
    
    # Check if all characters in the Gcode are the same
    same_digits = True
    for i in code:
        if i != code[0]:
            same_digits = False
            break
    if same_digits:
        return False
    
    # Validate the Gcode using a checksum algorithm
    a = int(code[9])  # Last digit of the code
    b = 0
    for i in range(0, 9): 
        b += int(code[i]) * (10 - i)  # Calculate weighted sum of the first 9 digits

    b = b % 11  # Modulo 11 operation on the sum
    # Validation logic based on the checksum
    if ((b >= 2 and a == 11 - b) or (b < 2 and a == b)):
        return True
    return False


def get_question(file_path, line_number):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for current_line, row in enumerate(csvreader, start=1):
            if current_line == line_number:
                return row
    return None  # If the line number is out of range


# HTML templates for login and logout options
loginOptions = """<a href="/signup" class="signup">
                    <li>
                        <p>ثبت نام</p>
                    </li>
                </a>
                <!-- login -->
                <a href="/login" class="login">
                    <li>
                        <p>ورود</p>
                    </li>
                </a>"""

logoutOptions = """<a href="/logout" class="login">
                    <li>
                        <p>خروج</p>
                    </li>
                </a>"""

# HTML templates for login and logout options on mobile
loginOptionsMobile = """<a href="/signup" class="signup">
                    <li>
                        <img src="../static/resources/Images/icons/header/icons8-sign-up-32.png" alt="">
                        <p>ثبت نام</p>
                    </li>
                </a>
                <a href="/login" class="login">
                    <li>
                        <img src="../static/resources/Images/icons/header/icons8-login-50.png" alt="">
                        <p>ورود</p>
                    </li>
                </a>"""

logoutOptionsMobile = """<a href="/logout" class="logout">
                    <li>
                        <img src="../static/resources/Images/icons/header/icons8-log-out-50.png" alt="">
                        <p>خروج</p>
                    </li>
                </a>"""