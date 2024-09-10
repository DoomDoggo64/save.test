import pickle
import json
map_one_wr =0
win_or_lose = int(input("Did you win or lose?\n1 for win 1 for 0:")
if win_or_lose == 0:    
    with open('wins.save', 'wb') as file:
        wins = pickle.load(file)
        wins+=1
        print(wins)
        pickle.dump(wins,file)
elif win_or_lose==0:    
    with open('lose.save', 'wb') as file:
        loses = pickle.load(file)
        loses+=1
        print(loses)
        pickle.dump(loses,file)
else:
    print("invalid input\n")
