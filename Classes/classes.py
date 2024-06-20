class User:
    def __init__(self, username, age, city):
        self.username = username
        self.age = age
        self.city = city

    def __str__(self):
        return f"(username='{self.username}', age={self.age}, city='{self.city}')"


user1 = User("Aftab", 21, "Solapur")
print(user1)


class User2(User):
    pass


user2 = User2("a", 21, "s")
print(user2)
