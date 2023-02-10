class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_attributes(self):
        """ a method to print all of an objects attributes """
        print(self.name, self.age, self.position, self.team)

    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for player in team_list:
            new_list.append(Player(player))
        return new_list



kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


# print the player objects's attributes
player_kevin.display_attributes()
player_jason.display_attributes()
player_kyrie.display_attributes()


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


new_team = []
# add Player objects made from players to new_team
for player_dict in players:
    new_team.append(Player(player_dict))

# print the player objects's attributes
for player_class in new_team:
    player_class.display_attributes()


# create a list of Player objects by using the Player class method
new_team2 = Player.get_team(players)

# print the player objects's attributes
for player_class in new_team2:
    player_class.display_attributes()
