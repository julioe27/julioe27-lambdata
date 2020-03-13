# example teams.py (functional approach)
# def advertise(my_team):
#     print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")
# def full_name(my_team):
#     return f"{my_team['city']} {my_team['name']}"
# if __name__ == "__main__":
#     teams = [
#         {"city": "New York", "name": "Yankees"},
#         {"city": "New York", "name": "Mets"},
#         {"city": "Boston", "name": "Red Sox"},
#         {"city": "New Haven", "name": "Ravens"},
#         {"city": "Washington", "name": "Nationals"}
#     ]
#     for team in teams:
#         print("-------")
#         print(full_name(team))
#         advertise(team)

class Team():
    # init = initilizater
    def __init__(self, name, city):
        self.name = name
        self.city = city

    # method
    def advertise(self):
        print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")

    # property
    @property
    # @property, what is this exactly?
    def full_name(self):
        return f"{self.city} {self.name}"


if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]
    for team_attributes in teams:
        team = Team(name=team_attributes["name"], city=team_attributes["city"])
        print("-------")
        # print(full_name(team))
        # advertise(team)
        print(team.city)
        print(team.full_name())
        team.advertise()

    # team = Team(city="Washington", name="Wizards") # initialize/ create an instance of the object
    # print(team)
    # print(type(team))
    # print(team.name) # invoking attributes
    # print(team.city) # invoking attributes
    # team2 = Team("Giants", "New York") # initialize/ create an instance of the object
    # print(team2)
    # print(type(team2))
    # print(team2.name) # invoking attributes
    # print(team2.city) # invoking attributes
