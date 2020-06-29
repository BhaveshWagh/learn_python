class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type    = cuisine_type
        self.number_served   = 0

    def describe_rastaurant(self):
        print(f"\nRestaurant name:  {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}\n")

    def set_number_served(self):
        print(f"\tThis restaurant has {self.number_served} customers")

    def increment_number_served(self, newly_added_served):
        print(f"\tNo of customers served{newly_added_served}\n")
        self.number_served += newly_added_served


restaurant = Restaurant("Gulgi","Mexican")
restaurant.describe_rastaurant()
restaurant.set_number_served()

restaurant.increment_number_served(33)
restaurant.set_number_served()

restaurant.increment_number_served(40)
restaurant.set_number_served()

restaurant.increment_number_served(37)
restaurant.set_number_served()




