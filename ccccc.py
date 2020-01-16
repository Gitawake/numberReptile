import random


class Role:
    def __init__(self, bv, bap, ga, us, c, cdr):
        self.Blood_volume = bv
        self.Basic_attack_power = bap
        self.General_attack = self.Basic_attack_power + ga
        self.Unique_skills = self.Basic_attack_power + us
        self.Critical = c
        self.Critical_damage_rate = cdr


Critical = random.randint(1, 100)

if Critical <= Role(100, 5, 3, 25, 25, 30).Critical:
    print('a')
else:
    print('b')
