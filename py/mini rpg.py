import random
import time

print("you have reached the opening of a cave you decide to arm yourself with a")

time.sleep(2)

quest_item = input("think of an object\n")

time.sleep(2)

print("you could not find", quest_item)
print("you select any item that comes to hand from the backpack instead\n")
time.sleep(3)

inventory = ["Torch","pencil","Rubber band","Catapult","Rope"]

print(random.choice(inventory))