# This code will randomly generate a password and is from the following website:  http://www.pythonforbeginners.com/code-snippets-source-code/script-password-generator

import string
from random import *
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(8,16)))
print(password)
