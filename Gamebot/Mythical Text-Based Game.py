player_name = input("Hello, traveler! Who might you be? \n")
ask_player_species = input("Well hello, {}! It is nice to meet you. You are very interesting. What are you? \n[a] Human \n[b] Elf \n[c] Orc \n".format(player_name))
def player_species_set():
    if ask_player_species == "a":
        player_species = "a human"
    elif ask_player_species == "b":
        player_species = "an elf"
    elif ask_player_species == "c":
        player_species = "an orc"
    return player_species
weapon_choice = input("Ah, you are {}. I thought so. What type of weapon would you like to choose? \n[a] Hammer \n[b] Sword \n[c] Knives \n".format(player_species_set()))
def weapon_choice_set():
    if weapon_choice == "a":
        player_weapon = "a hammer"
    elif weapon_choice == "b":
        player_weapon = "the sword"
    elif weapon_choice == "c":
        player_weapon = "some knives"
    return player_weapon
print("Yes, {}, good choice, {}. \n".format(weapon_choice_set(), player_name))