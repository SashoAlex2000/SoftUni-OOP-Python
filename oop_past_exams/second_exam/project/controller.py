

class Controller():
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        current_players = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                current_players.append(player)

        return "Successfully added: "+", ".join([player.name for player in current_players])

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        if sustenance_type not in ["Food", "Drink"]:
            pass
        else:
            for player in self.players:
                if player.name == player_name:
                    if not player.need_sustenance:
                        return f"{player_name} have enough stamina."

                    if sustenance_type == "Food":
                        for supply in reversed(self.supplies):
                            if supply.__class__.__name__ == "Food":
                                # player.stamina += supply.energy
                                if player.stamina + supply.energy >= 100:
                                    player.stamina = 100
                                else:
                                    player.stamina += supply.energy
                                current_supply_name = supply.name
                                self.supplies.pop(-1)
                                return f"{player_name} sustained successfully with {current_supply_name}."
                        raise Exception("There are no food supplies left!")

                    elif sustenance_type == "Drink":
                        for supply in reversed(self.supplies):
                            if supply.__class__.__name__ == "Drink":
                                player.stamina += supply.energy
                                if player.stamina >100:
                                    player.stamina = 100
                                current_supply_name = supply.name
                                self.supplies.pop(-1)
                                return f"{player_name} sustained successfully with {current_supply_name}."
                        raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name, second_player_name):
        first_player = ""
        second_player = ""

        for player in self.players:
            if player.name == first_player_name:
                first_player = player

        for player in self.players:
            if player.name == second_player_name:
                second_player = player

        will_duel = True
        result = f""
        if first_player.stamina <= 0:
            will_duel = False
            result += f"Player {first_player_name} does not have enough stamina."

        if second_player.stamina <= 0:
            will_duel = False
            result += f"Player {second_player_name} does not have enough stamina."

        if not will_duel:
            return result
        else:
            if first_player.stamina < second_player.stamina:
                attack_value = first_player.stamina / 2
                if second_player.stamina - attack_value <= 0:
                    second_player.stamina = 0

                    return f"Winner: {first_player.name}"
                else:
                    second_player.stamina -= attack_value

            # else:
                attack_value = second_player.stamina / 2
                if first_player.stamina - attack_value <= 0:
                    first_player.stamina = 0
                    
                    return f"Winner: {second_player.name}"

                else:
                    first_player.stamina -= attack_value

                if first_player.stamina > second_player.stamina:
                    return f"Winner: {first_player.name}"
                else:
                    return f"Winner: {second_player.name}"

            else:
                attack_value = second_player.stamina / 2
                if first_player.stamina - attack_value <= 0:
                    first_player.stamina = 0

                    return f"Winner: {second_player.name}"

                else:
                    first_player.stamina -= attack_value

                attack_value = first_player.stamina / 2
                if second_player.stamina - attack_value <= 0:
                    second_player.stamina = 0

                    return f"Winner: {first_player.name}"
                else:
                    second_player.stamina -= attack_value

                if first_player.stamina > second_player.stamina:
                    return f"Winner: {first_player.name}"
                else:
                    return f"Winner: {second_player.name}"


    def next_day(self):
        for player in self.players:
            reduction = 2 * player.age

            if player.stamina - reduction <= 0:
                player.stamina = 0
            else:
                player.stamina -= reduction

        for player in self.players:
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ""

        for player in self.players:
            result += f"{player.__str__()}\n"

        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}"

