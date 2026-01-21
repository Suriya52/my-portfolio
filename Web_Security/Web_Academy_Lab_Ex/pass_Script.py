"""This script generates a list of usernames and passwords
for a web security lab exercise.

It prints usernames and passwords in a specific format.

Example: carlos (worng user)
         carlos (wrong user)
         wiener(correct user)
         
This is because the website block the ip after 3 attempts so we did this scritpt to avoid that.
We made two attempts with the username "carlos" and one with "wiener"."""


"""This code is for the passwords.txt in the different folder as this script."""

"""print("###########The following are the usernames:###############")
for i in range(150):
    if i % 3:
        print("carlos")
    else:
        print("wiener")


print("##############The following are the passwords:############")
with open('passwords.txt', 'r') as f:
    lines = f.readlines()

i = 0
for pwd in lines:
    if i % 3:
        print(pwd.strip('\n'))
    else:
        print("peter")
        print(pwd.strip('\n'))
        i = i+1
    i = i +1 """





"""This code for the passwords.txt in the same folder as this script."""

import os

print("###########The following are the usernames:###############")
for i in range(150):
    if i % 3:
        print("carlos")
    else:
        print("wiener")

print("##############The following are the passwords:############")

# Get the absolute path to the 'passwords.txt' file in the same folder as this script
script_dir = os.path.dirname(__file__)  # The directory of the script
file_path = os.path.join(script_dir, 'passwords.txt')

# Read the password file
with open(file_path, 'r') as f:
    lines = f.readlines()

i = 0
for pwd in lines:
    if i % 3:
        print(pwd.strip('\n'))
    else:
        print("peter")
        print(pwd.strip('\n'))
        i = i + 1
    i = i + 1
