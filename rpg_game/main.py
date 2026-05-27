# python_practice_RPG
import pyinputplus as pyip
import random,time
player = {
    "name": "Hero",
    "hp": 100,
    "attack": random.randint(15,25),
    "inventory": ["potion"]
}

enemy = {
    "name": "Slime",
    "hp": 60,
    "attack": random.randint(10,30),
    "inventory": ["potion",'potion','potion']
}

# check information
def show_status(character):
    print(f'\ncharacter: {character["name"]}\nHP: {character["hp"]}')

# attack system
def attack(attacker,target):
    damage = attacker['attack']
    if target.get('defend') == True:
        damage = damage // 2
        print(f"{target['name']} defended the {attacker['name']}!")

    target['hp'] = target['hp'] - damage
    print(f"Now {target['name']} has {target['hp']} HP\n")
    target['defend'] = False
    time.sleep(0.5)
    return target, damage
    
# potion system 
def use_potion(character):
    if 'potion' in character['inventory']:
        character['hp'] = character['hp'] + 15
        character['inventory'].remove('potion')
        print(f'Now {character["name"]} has {character["hp"]} HP\n')
        time.sleep(0.5)
    else:
        print(f'Hahaha {character["name"]} don\'t have potion\n')
        time.sleep(0.5)
    return character

# Defend system
def defend(character):
    character['defend'] = True
    print(f'Now {character["name"]} is defending\n')


# Main loop
print('=====RPG=====')
while True:
    print('Your action:<1>defend, <2>attack, <3>potion', '<4>exit')
    show_status(player)
    show_status(enemy)
    time.sleep(0.5)

    # UserAction
    usersAction = pyip.inputChoice(['1','2','3','4'],prompt='What do you do: ')

    if usersAction == '1':
        defend(player)
    elif usersAction == '2':
        enemy , damage = attack(player,enemy)
    elif usersAction == '3':
        player = use_potion(player)
    elif usersAction == '4':
        break

    if enemy['hp'] <= 0:
        print('You win\n')
        break

    # EnemyAction
    enemyAction = random.randint(1,2)
    if enemyAction == 1:
        player , damage = attack(enemy,player)
        time.sleep(0.5)
        print(f"You lose {enemy['damage']} hp. You still have {player['hp']} hp\n")
        time.sleep(0.5)
    elif enemyAction == 2:
        enemy = use_potion(enemy)
        time.sleep(0.5)
        print(f'It has {enemy["hp"]} hp now')
        time.sleep(0.5)

    # Determine victory
    if player['hp'] <= 0:
        print('You lose\n')
        break
