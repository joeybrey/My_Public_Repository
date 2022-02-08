error_message = "Sorry, I did not get that. Please choose a valid item from the above list. \n"
player_name = input("Hello, traveler! Who might you be? \n")
def player_species_set():
    ask_player_species = input("Well hello, {}! It is nice to meet you. You are very interesting. What are you? \n[a] Human \n[b] Elf \n[c] Orc \n".format(player_name))
    if ask_player_species == "a":
        player_species = "a human"
    elif ask_player_species == "b":
        player_species = "an elf"
    elif ask_player_species == "c":
        player_species = "an orc"
    else:
        print(error_message)
        return player_species_set()
    return player_species
def weapon_choice_set():
    weapon_choice = input("Ah, you are a {}. I thought so. What type of weapon would you like to choose? \n[a] Hammer \n[b] Sword \n[c] Knives \n".format(ask_player_species))
    if weapon_choice == "a":
        player_weapon = "a hammer"
    elif weapon_choice == "b":
        player_weapon = "the sword"
    elif weapon_choice == "c":
        player_weapon = "some knives"
    else:
        print(error_message)
        return weapon_choice_set()
    return player_weapon
print("Yes, {}, good choice, {}. \n".format(weapon_choice_set(), player_name))