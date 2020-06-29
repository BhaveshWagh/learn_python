class User:

    def __init__(self, first_name, last_name,user_name,contact_no,email):
        self.first_name = first_name
        self.last_name  = last_name
        self.user_name  = user_name
        self.contact_no  = contact_no
        self.email      = email

    def describe_user(self):
        print(f"User full Name :{self.first_name} {self.last_name}")
        print(f"User name : {self.user_name}")
        print(f"Contact no: {self.contact_no}")
        print(f"email address : {self.email}")

    def greet_user(self):
        print(f"HELLO  Mr.{self.first_name}\n")

new_user = User("Mattew", "Murdock","mattew@27",9934243322,"mattew@2711.com")
new_user.describe_user()
new_user.greet_user()

another_user = User("Foggy", "Nelson","fogg@28",9785344433,"foggyNel@22.com")
another_user.describe_user()
another_user.greet_user()

