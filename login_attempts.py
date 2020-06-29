class User:

    def __init__(self, first_name, last_name,user_name,contact_no,email,login_attempts):
        self.first_name = first_name
        self.last_name  = last_name
        self.user_name  = user_name
        self.contact_no  = contact_no
        self.email      = email
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\n...User Information...\n")
        print(f"Name :  {self.first_name} {self.last_name}")
        print(f"\tUser name : {self.user_name}")
        print(f"\tContact no : {self.contact_no}")
        print(f"\temail address : {self.email}\n")
        print(f"User login attempts {self.login_attempts} times")

    def increment_login_attempts(self):
        print(f" Number of Login attempts : {self.login_attempts}")
        self.login_attempts += 1

    def reset_login_attempts(self,reset):
        print(f"Reset the Login attempts : {reset}\n ")

first_user = User("Mattew", "Murdock","mattew@27",9934243322,"mattew@2711.com",3)
first_user.describe_user()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.reset_login_attempts(0)

another_user = User("Foggy", "Nelson","fogg@28",9785344433,"foggyNel@22.com",2)
another_user.describe_user()
another_user.increment_login_attempts()
another_user.increment_login_attempts()
another_user.increment_login_attempts()
another_user.reset_login_attempts(0)

