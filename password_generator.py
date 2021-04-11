#coding-utf8
#Author: By HiFeV - 11/04/2021

import string
import random

length = int(input("Choose the length of the password: "))

letters = string.ascii_letters
digits =  string.digits
punctuation = string.punctuation

elements = letters + digits + punctuation
passwd = random.sample(elements, length)

result = "".join(passwd)
print("[+] Your password is: ", result)