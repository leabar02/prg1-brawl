import random

print("You are walking down the streets and suddenly you feel your heart pounding faster and faster. something is wrong but you don't know what then you feel it something is inside you.")
print("You remember you had that one spell that lets you go into your own body. You cast it and suddenly you are standing by your heart, it feels giant now that you are much smaller.")
print("Then you hear something, it sounds like something straight out of a horror movie. The thing that appears after that is a nightmare for the eyes, it has hairy legs and looks like a ball. ")
print("You now know what it is. It is a virus!")

du_hp = 500
virus_hp = 610

while du_hp > 0 and virus_hp > 0:
    du_spell = random.randint(5, 10)
    virus_spit = random.randint(15, 20)
    du_hp -= virus_spit
    virus_hp -= du_spell
    du_spell_crit = random.random(0 - 1)
    du_spell += du_spell_crit
    virus_hp -= du_spell_crit + du_spell
    print(f"Du: {max(0, du_hp)} HP  Fiende: {max(0, virus_hp)} HP")

while True:
    print("/n1. spell 1; kingslayer: wield the spear that deafeted the the devil and throw it, dealing massive amounts of dmg")
    print("2. spell 2; Avenging execution: dash with the speed of light, granting you + 20 dmg and crit dmg")
    print("3. spell 3:")
   

   
    if du_hp <= 0:
        du_hp += 250
        print("You are dead, but your will to live is to strong. You are granted a second chance ant life.")
    elif virus_hp == 100:
        print("You win, and Virus does suicide.")
    elif virus_hp < 100:
        virus_hp += du_spell
        print("The virus is nearing its end.")
        break
    else:
        print("continue fighting")


      


    









