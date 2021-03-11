import string
import random

def randompassword():
    chars = string.ascii_letters + string.digits
    size = 3

    return "".join(random.choice(chars) for x in range())