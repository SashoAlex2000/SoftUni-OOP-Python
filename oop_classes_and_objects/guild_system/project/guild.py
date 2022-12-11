from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."

        else:
            for curr_player in self.players:
                if curr_player.name == player.name:
                    return f"Player {player.name} is already in the guild."

            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()

        return result

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
#
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())


