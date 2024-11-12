# The program simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.
# Author: Joanna Kelly

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate a single round of battle
def battle_round():
    # Roll the dice
    attacker_rolls = np.random.randint(1, 7, size=3) # from numbers 1 up to but not including 7
    defender_rolls = np.random.randint(1, 7, size=2) # size determines how many numbers to generate

    # Sort rolls from highest to lowest
    attacker_rolls = np.sort(attacker_rolls)[::-1] # np.sort goes from ascending order
    defender_rolls = np.sort(defender_rolls)[::-1] # [::-1] slice reverses the order by starting at the end and going backwards

    attacker_losses = 0
    defender_losses = 0

    for i in range(min(len(attacker_rolls), len(defender_rolls))):
        if attacker_rolls[i] > defender_rolls[i]:
            defender_losses += 1
        else:
            attacker_losses += 1

    return attacker_losses, defender_losses

attacker_losses, defender_losses = battle_round()


# Number of rounds to simulate
num_rounds = 1000

total_attacker_losses = 0
total_defender_losses = 0

# Run the simulation for 1000 rounds
for _ in range(num_rounds):
    attacker_losses, defender_losses = battle_round()
    total_attacker_losses += attacker_losses
    total_defender_losses += defender_losses

# Print the totals
print(f"Total Attacker Losses: {total_attacker_losses}, Total Defender Losses: {total_defender_losses}")

score= np.array([total_attacker_losses, total_defender_losses])
mylabels = ["Attacker Losses", "Defender Losses"]
colours= ["red", "blue"]

plt.figure(figsize=(8, 8))
plt.pie(score, labels= mylabels, colors= colours, autopct= "%1.1f%%", startangle= 140)
plt.title("Proportion of Attacker Losses and Defender Losses")
plt.show()