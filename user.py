
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print("=====================================")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self


michael = User("Michael", "Sanchez", "mjs070594@gmail", "28")
batman = User("Bruce", "Wayne", "batmobile@gmail", "35")
superman = User("Clark", "Kent", "supes@gmail", "?")


michael.display_info().enroll().spend_points(50).display_info()
batman.enroll().spend_points(80).display_info()
superman.display_info()
