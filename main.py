import random
import os
import sys 
import string
notNum = False
print("Python Password Generator")
def numChecker(length):
  try:
    float(length)
  except ValueError:
    print("This is not a number")
    global notNum
    notNum = True
    
length = input("How long should the password be?\n")
numChecker(length)
while True:
  if notNum is True:
    os.execl(sys.executable, sys.executable, *sys.argv)
  else:
    specialChars = input("Do you want special Characters? (eg: !@#$)\n")
    yes = ["Yes", "yes", "YES", "y", "Y"]
    no = ["No", "No", "N", "n"]
    if specialChars in yes:
      chars = True
      numOfChars = input("Enter desired number of special Chars?\n")
      numChecker(numOfChars)
      regChars = int(length) - int(numOfChars)
      print(regChars)
      break
    if specialChars in no:
        print("Invalid selection, please enter Yes/No")
        continue
def shuffle_words(result_Chars, result_SpecialChars):
  concatenated_Str = result_Chars + result_SpecialChars
  str_var = list(concatenated_Str)
  random.shuffle(str_var)
  global result
  result = ''.join(str_var)
  
  return result
def passwordGenerator():
  if regChars > 1:
    global result_Chars
    result_Chars = ''.join(random.choice(string.ascii_letters) for i in range(regChars))
    print(result_Chars)
    global result_SpecialChars
    result_SpecialChars = ''.join(random.choice(string.punctuation) for i in range(int(numOfChars)))
    print(result_SpecialChars)
    shuffle_words(result_Chars, result_SpecialChars)
  else:
    result_SpecialChars = ''.join(random.choice(string.punctuation) for i in range(int(numOfChars)))
    print("Your password is:\n" + result_SpecialChars)
    
  
passwordGenerator()
  
  

