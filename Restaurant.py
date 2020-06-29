class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type

    def describe_rastaurant(self):
        print(f"Restaurant name:  {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant  is open now,  come on & "
              f"try it {self.cuisine_type} food\n")

new_restaurant = Restaurant("BM","Indian")

new_restaurant.describe_rastaurant()
new_restaurant.open_restaurant()

new_restaurant1 = Restaurant("Gulgi","Mexican")

new_restaurant1.describe_rastaurant()
new_restaurant1.open_restaurant()

new_restaurant2 = Restaurant("BBC","spanish")
new_restaurant2.describe_rastaurant()
new_restaurant2.open_restaurant()


