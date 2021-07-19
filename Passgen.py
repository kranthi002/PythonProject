import array
import random
MAX_LEN = 12
uppercase = ["A","B","C", "D","E","F","G","H", "I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol = ["!","@","#","$","%","^","&","*", "(", ")", "-", "_", "+"]
number = ["1","2","3","4","5","6","7","8","9","0"]

x = uppercase + lowercase + symbol + number

rand_upper = random.choice(uppercase)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(symbol)
rand_number = random.choice(number)

temp_pass = rand_number + rand_lower + rand_symbol + rand_upper

for i in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(x)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for j in temp_pass_list:
        password = password + x

print(password)