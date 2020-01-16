import random


class Role:

    def __init__(self, bv, bap, ga, us, c, cdr):
        self.Blood_volume = bv
        self.Basic_attack_power = bap
        self.General_attack = self.Basic_attack_power + ga
        self.Unique_skills = self.Basic_attack_power + us
        self.Critical = c
        self.Critical_damage_rate = cdr


class GameCombat:
    hero = Role(100, 5, 3, 25, 20, 30)
    villain = Role(150, 2, 2, 20, 20, 25)

    hero_current = hero.Blood_volume
    villain_current = villain.Blood_volume

    def damage_algorithm(self, c, cdr, ga):
        random_value = random.randint(1, 100)
        if random_value <= c:
            critical_hit_value = cdr / 100
            critical_hit_value = ga * critical_hit_value
            critical_hit_value = critical_hit_value + ga
            print('攻击触发了暴击造成{}点伤害。'.format(critical_hit_value))
            return critical_hit_value
        else:
            print('攻击造成{}点伤害。'.format(ga))
            return ga


GC = GameCombat()
print('开始游戏')
while GC.hero_current > 0 and GC.villain_current > 0:
    print("英雄      VS      反派\n血量：{:.0%}    血量：{:.0%}".format(GC.hero_current / GC.hero.Blood_volume,
                                                              GC.villain_current / GC.villain.Blood_volume))
    print("血量：{}点    血量：{}点".format(GC.hero_current, GC.villain_current))
    attack = input()

    if attack == '1':
        vga = GC.damage_algorithm(GC.villain.Critical, GC.villain.Critical_damage_rate, GC.villain.General_attack)
        GC.hero_current = GC.hero_current - vga
        if GC.hero_current <= 0:
            print('反派打败了英雄，游戏结束')
    elif attack == '2':
        vga = GC.damage_algorithm(GC.hero.Critical, GC.hero.Critical_damage_rate, GC.hero.General_attack)
        GC.villain_current = GC.villain_current - vga
        if GC.villain_current <= 0:
            print('英雄打败了反派，游戏结束')


