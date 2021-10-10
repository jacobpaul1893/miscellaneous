import random
import string

def gen_pass(stringLength=16):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

pwl = list(gen_pass(16))
#print(pwl)
random.shuffle(pwl)
pw = ''.join(pwl)
print(pw)
