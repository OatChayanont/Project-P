"""รวมตู้กาชาทั้งหมด"""
import random
def wish10pull():
    wish = []
    global garantee5
    global garantee4
    for _ in range(0, 10):
        if garantee5 >= 89:
            wish.append(get(5))
            garantee5 = 0
            garantee4 = 0
        elif garantee4 >= 9:
            wish.append(get(4))
            garantee5 += 1
            garantee4 = 0
        else:
            rate = random.uniform(0, 100)
            if rate <= 0.6:
                wish.append(get(5))
                garantee5 = 0
            elif rate <= 5.1:
                wish.append(get(4))
                garantee5 += 1
                garantee4 = 0
            else:
                wish.append(get(3))
                garantee5 += 1
                garantee4 += 1
    wish.sort(reverse=True)
    return wish

def get(rarity):
    if rarity == 5:  # 0.6%
        if random.random() < 0.5:
            return '[5★] ' + random.choice(five_star_char)
        else:
            return '[5★] ' + random.choice(five_star_weapon)
    elif rarity == 4:  # 5.1%
        if random.random() < 0.5:
            return '[4★] ' + random.choice(four_star_char)
        else:
            return '[4★] ' + random.choice(four_star_weapon)
    elif rarity == 3:  # 94.3%s
        return '[3★] ' + random.choice(three_star_weapon)

def wish1pull():
    wish = []
    global garantee5
    global garantee4
    for _ in range(1):
        if garantee5 >= 89:
            wish.append(get(5))
            garantee5 = 0
            garantee4 = 0
        elif garantee4 >= 9:
            wish.append(get(4))
            garantee5 += 1
            garantee4 = 0
        else:
            rate = random.uniform(0, 100)
            if rate <= 0.6:
                wish.append(get(5))
                garantee5 = 0
            elif rate <= 5.1:
                wish.append(get(4))
                garantee5 += 1
                garantee4 = 0
                
            else:
                wish.append(get(3))
                garantee5 += 1
                garantee4 += 1
    return wish

global five_star_char
five_star_char = ['Jean', 'Qiqi', 'Keqing', 'Mona', 'Dilluc']
global four_star_char
four_star_char = ['Sayu', 'Sucrose', 'Rosaria', 'Diona', 'Chonyun', 'Kaeya', 'Kujou Sara', 'Fischl', 'Beidou', 'Razor',
                'Lisa', 'Nolle', 'Ningguang', 'Xingqiu', 'Barbara', 'Yanfei', 'Xinyan', 'Bennett', 'Xiangling', 'Amber']
global five_star_weapon
five_star_weapon = ['Skyward Harp', 'Amos\' Bow', 'Skyward Atlas', 'Lost Prayer to the Sacred Winds', 'Skyward Pride',
                    'Wolf\'s Gravestone', 'Skyward Spine', 'Primordial Jade Winged-Spear', 'Skyward Balde', 'Aqulia Favonia']
global four_star_weapon
four_star_weapon = ['Favonius Warbow', 'Sacrificial Bow', 'The Stringless', 'Rust', 'Favonius Codex', 'Sacrificial Fragments', 'The Widsith', 'Eye of Perception',
                    'Favonius Greatsword', 'Sacrificial Greatsword', 'The Bell', 'Rainslasher', 'Favonius Lance', 'Dragon\'s Bane', 'Favonius Sword', 'Sacrificial Sword', 'The Flute', 'Lion\'s Roar']
global three_star_weapon
three_star_weapon = ['Slingshot', 'Sharpshooter\'s Oath', 'Raven Bow', 'Emerald Orb', 'Thrilling Tales of Dragon Slayers', 'Magic Guide',
                    'Debate Club', 'Bloodtainted Greatsword', 'Ferrous Shadow', 'Black Tassel', 'Skyrider Sword', 'Harbinger of Dawn', 'Cool Steel']
global garantee5
garantee5 = 0
global garantee4
garantee4 = 0
