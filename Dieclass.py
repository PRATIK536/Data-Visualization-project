import random

# Roll six dice
def roll_six_dice():
    dice_results = []
    for i in range(6):
        roll = random.randint(1, 6)
        dice_results.append(roll)
        print(f"Die {i+1}: {roll}")
    return dice_results

# Run the program
print("🎲 Rolling 6 dice...")
results = roll_six_dice()




