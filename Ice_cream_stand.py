class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name:  {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} Icecream House is open,  come on & "
              f"try it {self.cuisine_type} food\n")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type= "icecream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("The following flavors are available : ")
        for flavor in self.flavors:
           print(f"{flavor}")


restaurant = IceCreamStand('Gulgi')

restaurant.flavors = ["chocalate chips","strawberry","vanilla"]
restaurant.describe_restaurant()
restaurant.display_flavors()


