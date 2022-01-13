poke_party = ["PIKACHU", "CHARMELEON", "GEODUDE", "GYARADOS", "BUTTERFREE", "MANKEY"]

while True:
    print("EXCHANGE POKEMON\n")
    for i in range(len(poke_party)):
        print(f"\t{i}. {poke_party[i]}")

    print(f"\nChoose a Pokemon (Or -1 to quit.)")
    a = int(input("> "))

    if a == -1:
        break

    print(f"Choose a Pokemon to exchange with {poke_party[a]}")
    b = int(input("> "))
    
    print(f"\nExchanging {poke_party[a]} with {poke_party[b]}.\n")

    # add code here to swap the Pokemon in slot a with the Pokemon in slot b
    pokemon = poke_party[a]
    poke_party[a] = poke_party[b]
    poke_party[b] = pokemon
