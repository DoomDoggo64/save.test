import pickle
import os
def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
def commands():
    print("Commands You Can Do\n.........................................................................")
    print("start: intializes your saves")
    print("reset: resets all of our save files to 0")
    print("win rate: updates your winrate")
    print("exit: ends the program")
    print("list: lists all commands")
    print("display: displayes your winrate")
    print("display_rank: displayes your rank")
    print("update_rank: updates your rank")
    print("clear_terminal: clears the terminal")
    print("maps: list the valid maps")
    print(".........................................................................")
dorado = ['dorado_wins.save','dorado_loses.save']
kings_row = ['kings_row_wins.save','kings_row_loses.save']
antartic=['antartic_wins.save','antartic_loses.saves']
busan = ['busan_wins.save','busan_loses.save']
nepal= ['nepal_wins.save','nepal_loses.save']
toa = ['toa_wins.save','toa_loses.save']
suravasa = ['suravasa_wins.save','suravasa_loses']
new_queens_street = ['new_queens_street_wins.save','new_queens_street_loses.save']
junkertown = ['junkertown_wins.save','junkertown_loses.save']
nubani=['nubani_wins.save','nubani_loses.save']
ilios=['ilios_wins.save','ilios_loses.save']
lijiang_tower=['lijiang_tower_wins.save','lijiang_tower_wins.save']
oasis=['oasis_wins.save','oasis_loses.save']
samoa=['samoa_wins.save','samoa_loses.save']
circuit_royal=['circuit_royal_wins.save', 'circuit_royal_loses.save']
havana=['havana_wins.save','havana_loses.save']
route_66=['route_66_wins.save','route_66_loses.save']
rialto=['rialto_wins.save','rialto_loses.save']
shambali=['shambali_wins.save','shambali_loses.save']
gibralter=['gibralter_wins.save','gibralter_loses.save']
blizz_world=['blizz_world_wins.save','blizz_world_loses.save']
eichenwalde=['eichenwalde_wins.save','eichenwalde_loses.save']
hollywood=['hollywood_wins.save','hollywood_loses.save']
midtown=['midtown_wins.save','midtown_loses.save']
paraiso=['paraiso_wins.save','paraiso_loses.save']
colosseo=['colosseo_wins.save','colosseo_loses.save']
runasapi=['runasapi_wins.save','runasapi_loses.save']
esperanca=['esperanca_wins.save','esperanca_loses.save']
alls=['wins.save','lose.save']
Maps= {
     "Dorado": dorado,
     "Kings Row": kings_row,
     "Antartic": antartic,
     "Nepal": nepal,
     "Busan": busan,
     "Throne of Anubis": toa,
     "Suravasa": suravasa,
     "New Queens Street": new_queens_street,
     "Junkertown": junkertown,
     "Nubani": nubani,
     "Ilios": ilios,
     "Lijiang Tower": lijiang_tower,
     "Oasis": oasis,
     "Samoa": samoa,
     "Circuit Royal": circuit_royal,
     "Havana": havana,
     "Rialto": rialto,
     "Route 66": route_66,
     "Shambali": shambali,
     "Gibraltar": gibralter,
     "Blizzard World": blizz_world,
     "Eichenwalde": eichenwalde,
     "Hollywood": hollywood,
     "Midtown": midtown,
     "Paraiso": paraiso,
     "Colosseo": colosseo,
     "Runasapi": runasapi,
     "Esperanca": esperanca
}
def initial_setup():
    for maps in Maps:
        saves= Maps[maps]
        with open(saves[0], 'wb') as file:
             pickle.dump(0,file)
        with open(saves[1], 'wb') as file:
             pickle.dump(0,file)
    with open(alls[0], 'wb') as file:
        pickle.dump(0,file)
    with open(alls[1], 'wb') as file:
        pickle.dump(0,file)
def win_rate_map(map,win_or_lose2):   
    if map in Maps:
        saves= Maps[map]
    else:
        print("invalid map\n type maps to see all the maps")
        return
    win_or_lose = win_or_lose2
    #updates global win rate
        #loads save file for wins
    with open(alls[0], 'rb') as file:
        wins = pickle.load(file)
    #loads save file for loses
    with open(alls[1], 'rb') as file:
            loses = pickle.load(file)
    if win_or_lose == "win":
        with open(alls[0], 'wb') as file:
            wins += 1
            pickle.dump(wins, file)
    elif win_or_lose == "lose":
        with open(alls[1], 'wb') as file:
            loses += 1
            pickle.dump(loses, file)
    else:
        print("invalid input\n")
        return
    with open(saves[0], 'rb') as file:
                wins_map = pickle.load(file)
    #loads save file for loses
    with open(saves[1], 'rb') as file:
            loses_map = pickle.load(file)
    if win_or_lose == "win":
        with open(saves[0], 'wb') as file:
            wins_map += 1
            pickle.dump(wins, file)
    elif win_or_lose == "lose":
        with open(saves[1], 'wb') as file:
            loses_map += 1
            pickle.dump(loses, file)
    else:
        print("invalid input\n")
        return
    print("Wins for this map:", wins_map)
    print("Loses for this map:", loses_map)
    print("Win Rate for this map", round((wins_map/(loses_map+1))*100,2),"%")
def winrate():
    map = input("What map do you want to change?\nType all to effect the global win rate or type end to go back:")
    if map not in Maps:
         print("invalid map\n type maps to see all the maps")
         return
    win_or_lose = input("Did you win or lose?: ")
   #updates global win rate
    if map == "all":
        saves=alls
         #loads save file for wins
        with open(saves[0], 'rb') as file:
                wins = pickle.load(file)
        #loads save file for loses
        with open(saves[1], 'rb') as file:
                loses = pickle.load(file)
        if win_or_lose == "win":
            with open(saves[0], 'wb') as file:
                wins += 1
                pickle.dump(wins, file)
        elif win_or_lose == "lose":
            with open(saves[1], 'wb') as file:
                loses += 1
                pickle.dump(loses, file)
        else:
            print("invalid input\n")
            return
        print("Wins:", wins)
        print("Loses:", loses)
        print("Win Rate", round((wins/(loses+1))*100,2),"%")
    # goes back  
    elif map == "end":
         return
    else: 
         win_rate_map(map,win_or_lose)
def display():
    saves=alls
    with open(saves[0], 'rb') as file:
        wins = pickle.load(file)
    with open(saves[1], 'rb') as file:
        loses = pickle.load(file)
    print("Wins:", wins)
    print("Loses:", loses)
    print("Win Rate", round((wins/(loses+1))*100,2),"%")
def reset_rank():
     with open('rank.save', 'wb') as file:
        pickle.dump(0,file)
def display_rank():
    rank=""
    with open('rank.save', 'rb') as file:
        rank=pickle.load(file)
        print("current rank: ",rank)

def update_rank():
    with open('rank.save', 'rb') as file:
        rank = pickle.load(file)
    updated_rank=input("What rank are you currently?: ")
    with open('rank.save', 'wb') as file:
        pickle.dump(updated_rank,file)
    print("Previous rank: ", rank)
    print("Updated rank: ",updated_rank)

def what_is_next():
    whats_next=input("what do you want to do?\n:")
    if whats_next == "list":
        commands()
        what_is_next()
    elif whats_next == "win rate":
        winrate()
        what_is_next()
    elif whats_next == "exit":
        clear_terminal()
        print("ended program")
    elif whats_next == "display":
         display()
         what_is_next()
    elif whats_next == "start":
         initial_setup()
         reset_rank()
         print("Save files loaded")
         what_is_next()     
    elif whats_next == "maps":
         for maps in Maps:
              print(maps)
         what_is_next()
    elif whats_next == "reset":
         initial_setup()
         print("Save files reset")
         what_is_next()
    elif whats_next == "display_rank":
         display_rank()
         what_is_next()
    elif whats_next == "update_rank":
         update_rank()
         what_is_next()
    elif whats_next == "clear_terminal":
         clear_terminal()
         what_is_next()
    else: 
         print("not a valid command")
         print("type list for a full list of commands")
         what_is_next()
clear_terminal()
commands()
what_is_next()