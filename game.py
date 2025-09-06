import random
from goblin import Goblin
from hero import Hero
from Goblin_GiantBoss import Goblin_Giant
from Dart_Goblin import Dart_Goblin
def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Mega Knight")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(random.randint(3,4))]
    goblins.append(Dart_Goblin("Dart_Goblin"))
    Total_Goblins = len(goblins)
    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    GoblinDamage = 0
    HeroDamage = 0
    Number_Rounds = 0
    Round_Number = 1

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print(f"\nNew Round! Round:  {Round_Number}")
        Round_Number += 1
        Number_Rounds += 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        HeroDamage += damage
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!          !!! LIKE A BOSS !!!")
            

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                GoblinDamage += damage
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the basic goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive():
        Total_Goblins += 1
        print("             Round 10             ")
        Round_Number += 1
        print("***********Boss Fight Time**************")
        Goblin_GiantBoss = Goblin_Giant("Goblin_Giant")
        while hero.is_alive() and Goblin_GiantBoss.is_alive():
            damage = hero.strike()
            print(f"Hero attacks Goblin Giant for {damage} damage!")
            Goblin_GiantBoss.take_damage(damage)
            HeroDamage += damage
            damage = Goblin_GiantBoss.attack()
            print(f"Goblin Giant attacks hero for {damage} damage!")
            hero.receive_damage(damage)
            GoblinDamage += damage
        if hero.is_alive():
            defeated_goblins += 1
            print("The hero has defeated the Boss")
        else:
            print("The hero was defeated by the Boss")



    # Final tally of goblins defeated
    print("\nBattle Summary: ")
    print(f"\nTotal Damage Dealt: {int(HeroDamage + GoblinDamage)}")
    print(f"\nRounds Survived: {(Number_Rounds)}")
    print(f"\nTotal goblins defeated: {(defeated_goblins)} / {(Total_Goblins)}")

if __name__ == "__main__":
    main()
