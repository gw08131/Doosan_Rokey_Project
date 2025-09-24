# random_module.py

import random

animals= ['채셔고양이','오리','도도새']
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))

print("-----------------------------")
print(random.sample(animals,2))
print(random.sample(animals,2))
print(random.sample(animals,2))

print("-----------------------------")
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))