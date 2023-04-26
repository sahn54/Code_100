# To create a Class
# class Car:

# BluePrint
class User:
    # Attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created...")
    # Methods

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Sung")
user_2 = User("002", "Melissa")
print(user_1.id)  # type: ignore

# Constructor - initializing an object
# __init__(self):
#
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
