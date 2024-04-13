from art import logo 
from art import vs
from game_data import data
import random

def game():
  score = 0

  game_over = False
  while not game_over:

    print(logo)
    
    random_numberA = random.randint(0,len(data)-1)
    text_numberA = print(f"Compare A: {data[random_numberA]['name']}, {data[random_numberA]['description']}, {data[random_numberA]['country']}")
    personA = (int(data[random_numberA]["follower_count"]))
    
    print(text_numberA)

    print(vs)

    random_numberB = random.randint(0,len(data)-1)
    text_numberB = print(f"Compare B: {data[random_numberB]['name']}, {data[random_numberB]['description']}, {data[random_numberB]['country']}")
    personB = (int(data[random_numberB]["follower_count"]))

    print(text_numberB)

    answer = input("Who has more followers? Type 'A' or 'B':'")

    if (personA > personB and answer == "A") or (personA < personB and answer == "B"):
      score = score +1
      print(f"You are right, current score: {score}")

    else: 
      return (f"Sry thats wrong, final score: {score}")
      game_over = True

print(game())