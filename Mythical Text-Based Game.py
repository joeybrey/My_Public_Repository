player_name = input("Hello, traveler! Who might you be? \n")
print("Well hello, {}! It is nice to meet you".format(player_name))
ask_player_species = input("You are very interesting. What are you? \n[a] Human \n[b] Elf \n[c] Orc \n")
def player_species_set():
    if ask_player_species == "a":
        player_species = "a Human"
    elif ask_player_species == "b":
        player_species = "an Elf"
    elif ask_player_species == "c":
        player_species = "an Orc"
    return player_species
print("Ah, you are {}. \n".format(player_species_set()) + "That\'s right. I thought so. \n")
