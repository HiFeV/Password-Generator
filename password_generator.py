#coding-utf8
#Author: By HiFeV - 11/04/2021

import string
import random
import time

length = int(input("Choose the length of the password: "))

letters = string.ascii_letters
digits =  string.digits
punctuation = string.punctuation

elements = letters + digits + punctuation
passwd = random.sample(elements, length)

result = "".join(passwd)
print("[+] Your password is: ", result)

ask = input("Do you want to save your password in a textfile ? YES / NO: ")


if ask == "NO":
	print("Exiting...")
	time.sleep(3)
	exit()

elif ask == "YES":
	reminder = open("generated_password.txt", "w")
	text_file = reminder.write(result)
	reminder.close()
	print("[+] generated_password.txt successfully saved")
	print("Exiting...")
	time.sleep(3)
	exit()

else:
	print("You can only answer YES or NO")
	print(ask)
