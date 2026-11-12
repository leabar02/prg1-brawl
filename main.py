import random

spelare_hp = 210
fiende_hp = 300

while spelare_hp > 0 and fiende_hp > 0:
    spelare_slag = random.randint(1, 7)
    fiende_slag = random.randint(1, 10)
    spelare_crit = random.randint(10, 15)
    fiende_crit = random.randint(11, 17)
    spelare_super_crit = random.randint(20, 25)
    fiende_hp -= spelare_slag
    fiende_hp -= spelare_crit
    fiende_hp -= spelare_super_crit
    spelare_hp -= fiende_slag
    spelare_hp -= fiende_crit
    print(f"Du: {max(0,spelare_hp)} HP | Fiende: {max(0,fiende_hp)} HP")

if spelare_hp > 0:
    print("Du vann!")
else:
    print("Fienden vann.")
    










