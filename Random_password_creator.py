import random
import string

def pass_easy():
    common= open("1000-most-common-passwords.txt", "r").read()
    lst = common.split("\n")
    return print(random.choice(lst))

def pass_medium():
    length = int(input("How many characters do you want in your password?\n"))
    password = ""
    for i in range(length):
        rdm = random.randint(1,2)
        if rdm == 1 :
            password += random.choice(string.ascii_letters)
        if rdm == 2 : 
            password += str(random.randint(0,9))

    return print(password)

def pass_hard():
    length = int(input("How many characters do you want in your password?\n"))
    password = ""
    for i in range(length):
        rdm = random.randint(0, 1000)
        if rdm <= 500 :
            password += random.choice(string.ascii_letters)
        if 500 < rdm <= 800 : 
            password += str(random.randint(0,9))
        if rdm > 800 :
            password += random.choice(string.punctuation)
        
    return print(password)


def pass_gen():
    level = input("Easy, medium or hard password ? (write it)\n")
    if level.lower() == "easy":
        pass_easy()

    if level.lower() == "medium":
        pass_medium()

    if level.lower() == "hard":
        pass_hard()


pass_gen()
