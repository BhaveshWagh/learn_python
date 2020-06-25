import  pizza
pizza.pizza_menu()
pizza.make_pizza("large ","tomato","olives","onion")
pizza.make_pizza("samll","mushroom","onion","panner","chees")
print("-" * 200)

from pizza import make_pizza, pizza_menu
pizza_menu()
make_pizza("large ","tomato","olives","onion")
make_pizza("samll","mushroom","onion","panner","chees")
print("-" * 200)

from pizza import make_pizza
from pizza import pizza_menu as pm

pm()
make_pizza("large ","tomato","olives","onion")
make_pizza("samll","mushroom","onion","panner","chees")
print("-" * 200)

import pizza as pz
pz.pizza_menu()
pz.make_pizza("large ","tomato","olives","onion")
pz.make_pizza("samll","mushroom","onion","panner","chees")
print("-" * 200)

from pizza import * #it imports all functions
pizza_menu()
make_pizza("large ","tomato","olives","onion")
make_pizza("samll","mushroom","onion","panner","chees")



