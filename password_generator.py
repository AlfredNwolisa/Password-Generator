import string
import random
from getpass import getpass as input

upper_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)
symbols = list(string.punctuation)
numb = list(map(str, range(0, 10)))

#user input requirement
len_upper_letters = int(input("how many upper case letters will you like? "))
len_lower_letters = int(input("how many lower case letters will you like? "))
len_symbol =  int(input("how many upper symbols will you like? "))
len_numb = int(input("how many numbers will you like? "))

# main password generation function
def password_generator(len_upper_letters, len_lower_letters, len_symbol, len_numb):
   pwd = []

   for u in range(len_upper_letters): 
      pwd += random.choice(upper_letters)
   for low in range(len_lower_letters):
      pwd += random.choice(lower_letters)
   for s in range(len_symbol):
      pwd += random.choice(symbols)
   for n in range(len_numb):
      pwd +=  random.choice(numb)
      pwd_exchange = random.shuffle(pwd)
      password = "".join(pwd)
   return password
#return pwd

generated_password = password_generator(len_upper_letters, len_lower_letters, len_symbol, len_numb)
                                    

print("Your generated password is:", generated_password)
    