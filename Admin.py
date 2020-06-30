class User:

    def __init__(self, first_name, last_name,user_name,contact_no,email):
        self.first_name = first_name
        self.last_name  = last_name
        self.user_name  = user_name
        self.contact_no  = contact_no
        self.email      = email

    def describe_user(self):
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"User name : {self.user_name}")
        print(f"Contact no: {self.contact_no}")
        print(f"email address : {self.email}\n")

    def greet_user(self):
        print(f"HELLO  Mr.{self.first_name}\n")

class Admin(User):

    def __init__(self,first_name, last_name,user_name,contact_no,email):
        super().__init__(first_name, last_name,user_name,contact_no,email)
        self.privileges = []

    def show_privileges(self):
        print("privileges:")
        for privilege in self.privileges:
            print(f" * {privilege}")

new_user = Admin("Mattew", "Murdock","mattew@27",9934243322,"mattew@2711.com")
new_user.describe_user()

new_user.privileges = ['can reset passwords','blocke userid','delete post','add post']

new_user.show_privileges()
