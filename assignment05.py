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

print(f"Attacker Losses: {attacker_losses}, Defender Losses: {defender_losses}")
