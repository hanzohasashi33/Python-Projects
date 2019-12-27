import string
import random


def password_generator():
  caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  small = "abcdefghijklmnopqrstuvwxyz"
  numbers = "0123456789"
  special = "!@#$%^&*()_+=-{}[]|/?><,."


  passlen = input("ENTER YOUR PASSWORD LENGTH : ")
  no_caps = input("ENTER YOUR REQUIRED NUMBER OF CAPITAL LETTERS IN PASSWORD : ")
  no_small = input("ENTER YOUR REQUIRED NUMBER OF SMALL LETTERS IN PASSOWRD :")
  no_nos = input("ENTER YOUR REQUIRED NUMBER OF NUMBERS IN PASSWORD : ")
  no_spec = input("ENTER YOUR REQUIRED NUMBER OF SPECIALS IN PASSWORD : ")

  if(no_caps + no_small + no_nos + no_spec > passlen or no_caps + no_small + no_nos + no_spec < passlen):
    print "WRONG INPUT INFO,PLEASE TRY AGAIN LATER!!!"

  else:
    password = ''
    i = 0
    for i in range(no_caps):
        password += random.choice(caps)
    i = 0
    for i in range(no_small):
        password += random.choice(small)
    i = 0
    for i in range(no_nos):
        password += random.choice(numbers)
    i = 0
    for i in range(no_spec):
        password += random.choice(special)
    jumble = ""
    while password:
        position = random.randrange(len(password))
        jumble += password[position]
        password = password[:position] + password[(position + 1):]
    return jumble
    

if __name__ == '__main__':
  test_cases = input("how many passwords do you want:")
  j = 0
  l = []
  for j in range(test_cases):
    l.append(password_generator())
  for passwords in l:
    print passwords
