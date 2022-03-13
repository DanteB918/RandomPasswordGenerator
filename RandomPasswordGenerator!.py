import random
import string
print('Random Password Generator!')
#or print(random.randint(string.digits))
all = string.ascii_letters + string.digits

length = random.randint(8, 10)
password = random.sample(all, length)

password ="".join(password)
print(password)

