import pizza, random #methode 1 pour ImportError
pizza.make-pizza()
print(random.randint)

print(pizza.name)

from pizza import make_pizza, name #2e facon c ne pese pas beaucoup compare a methode 1 
make_pizza()
print(name)

import string as s #3e facon
