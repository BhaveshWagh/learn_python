from user import User

class Admin(User):
    def __init__(self,first_name, last_name,user_name,contact_no,email):
        super().__init__(first_name, last_name,user_name,contact_no,email)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges_items = ["can add post","can delete post","block user id","reset password"]

    def show_privileges(self):
        print("Admin sets the privileges to you:\n")
        for items in self.privileges_items:
            print(f"*{items}")

admin = Admin("Mattew", "Murdock","mattew@27",9934243322,"mattew@2711.com")

admin.describe_user()
admin.privileges.show_privileges()


