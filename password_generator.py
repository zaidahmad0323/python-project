import random
numbers=['0','1','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_']
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

no_letters=int(input("How many letters do you want in you password : "))
no_numbers=int(input("How many numbers do you want in you password : "))
no_symbols=int(input("How many symbols do you want in you password : "))

password_list=[]

for letter in range(no_letters+1):
    password_list +=random.choice(letters)
    
for number in range(no_numbers+1):
    password_list +=random.choice(numbers)
    
for symbol in range(no_symbols+1):
    password_list +=random.choice(symbols)
    
random.shuffle(password_list)

password=""

for char in password_list:
    password += char    
print(f"Your password is {password}")    