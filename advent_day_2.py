import sys

def check_valid_password(line):
    """Check if password input is valid. 
    Returns boolean.
    """

    value, char, password = line.split(" ")
    min_val, max_val = value.split("-")
    min_val = int(min_val)
    max_val = int(max_val)
    char = char.strip(":")
    password = password.strip()

    occurences_of_char = password.count(char)

    if occurences_of_char >= min_val and occurences_of_char <= max_val:
        return True
    else:
        return False

if __name__ == "__main__":
    """
    Excepted Input for Input file (space delimited):
        range target_char: password
        i.e.
        6-10 b: fskfhjfeijs
    """

    with open(sys.argv[1], 'r') as input_file:
        valid_passwords = 0
        for line in input_file:
            valid_password = check_valid_password(line)
            if valid_password:
                valid_passwords += 1
        print(valid_passwords)
