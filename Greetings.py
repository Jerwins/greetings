import string
from random import choice
from time import sleep

# Gathers all characters that should be shown during the message

digit_list = "".join(
    (string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation)
)

# Defining the colors of the text in bash

CBLINK = "\033[5m"
CRED = "\33[31m"
CEND = "\033[0m"
GRN = "\33[92m"
BOLD = " \33[1m"
WHITE = "\33[97m"

# The actual greeting message

text = " Have a happy new year 2020 \n"

print("\n")

for i, x in enumerate(text):
    for digit in digit_list:
        if digit != x:
            print(
                "\r",
                ("".join(choice(digit_list) for _ in range(len(text) - 1))),
                text[:i],
                end="",
                sep=(BOLD + CRED + CBLINK + "\r Message from Jerwin: " + CEND),
                flush=True,
            )
        sleep(0.0035)

print("\n")
print("\n")
