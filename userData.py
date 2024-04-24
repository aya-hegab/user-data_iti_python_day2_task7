import re

def isStringOnly(strIn):
  flag = 1
  for chr in strIn:
    if chr.isdigit():
      flag = 0
  return flag

def userInputs():
  nameUse = input("enter your name ")
  while len(nameUse) == 0 or not isStringOnly(nameUse):
    nameUse = input("enter your name ")
  daName = nameUse

  emailUse = input("enter your email ")
  while len(emailUse) == 0 or not re.fullmatch( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', emailUse):
    emailUse = input("enter your email ")
  daEmail = emailUse
  return daName, daEmail

def userData(nameIn, emailIn):
  return f"your name is {nameIn}\nyour email is {emailIn}"

userName, userEmail = userInputs()

print(userData(userName, userEmail))
