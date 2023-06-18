# imports that are real important

import datetime as dtm
import os
import random as rnd
import sys
import time as tm

# vars for the start of game

s = tm.time()
score = 0


hp = 100

joehp = 400

hunger = 100

enemyhp = 50  # it will be modified for every enemy

elaptime = 0

inventory = {"sandwich": 1}

weapon = {}

broomdamage = [5, 10, 15, 20]

bowdamage = [10, 13, 18, 25]

sworddamage = [90, 100, 200, 300]

joedamage = [50, 60, 65, 100]

joeturn_choose = ["attack", "defend"]

enemies = [
    "moth",
    "some yellow rat called achoo idk he from pokeyman",
    "thefinal boss, the blue gopro looking robot that has some funni guns",
]

mothdamage = [10, 13, 14, 18]

achoodamage = [20, 24, 26, 35]

theblugoprodamage = [90, 150, 200, 250]

enemyattackchoose = ["you", "joe"]


# defs to make the coding much easier


def prause(words):
    print(words)
    tm.sleep(2)


def retryask(tm):
    prause(f"you lose your score is {score} and you finished this ending in {tm}")

    m = input("do you want to retry? Y/N")

    if m == "Y" or m == "y":
        os.execl(sys.executable, sys.executable, f'"{sys.argv[0]}"')

    elif m == "N" or m == "n":
        sys.exit(1)


def retrytime_record():
    et = tm.time()

    el = et - s

    d = dtm.timedelta(seconds=el)

    dstr = str(d)

    retryask(dstr)


yourturn = 1

joeturn = 0

enemyturn = 0


def FIGHTMODE(hitthing, enemy):
    global yourturn

    global joeturn

    global enemyturn

    global hp

    global joehp

    global enemyhp

    while (hp > 0 or joehp > 0) and enemyhp > 0:
        broom_crit_chance = rnd.choices(population=broomdamage, weights=[40, 30, 20, 6])

        bow_crit_chance = rnd.choices(population=bowdamage, weights=[40, 30, 20, 6])[0]

        sword_crit_chance = rnd.choices(
            population=sworddamage, weights=[40, 40, 50, 30]
        )[0]

        moth_crit_chance = rnd.choices(population=mothdamage, weights=[40, 30, 20, 6])[
            0
        ]

        achoo_crit_damage = rnd.choices(
            population=achoodamage, weights=[40, 30, 20, 6]
        )[0]

        gopro_crit_damage = rnd.choices(
            population=theblugoprodamage, weights=[40, 30, 20, 6]
        )[0]

        joes_crit_chance = rnd.choices(population=joedamage, weights=[50, 40, 40, 10])[
            0
        ]

        joes_choose_chance = rnd.choices(population=joeturn_choose, weights=[40, 60])[0]

        enemychoose_chance = rnd.choices(
            population=enemyattackchoose, weights=[50, 50]
        )[0]

        print(f"{hp=} {joehp=} {enemyhp=}")

        if yourturn == 1:
            decide = input(
                "ITS YOUR TURN YOU CAN EITHER A)ATTACK OR B)DEFEND(increases hp)"
            )

            if decide == "A" or decide == "a":
                if hitthing == "broom":
                    prause(f"YOU ATTACK ENEMY -{broom_crit_chance}")

                    enemyhp -= broom_crit_chance[0]

                    prause(f"ENEMY HP:{enemyhp}")

                    yourturn -= 1

                    joeturn += 1

                elif hitthing == "bow":
                    prause(f"YOU ATTACK ENEMY -{bow_crit_chance}")

                    enemyhp -= bow_crit_chance

                    prause(f"ENEMY HP:{enemyhp}")

                    yourturn -= 1

                    joeturn += 1

                elif hitthing == "sword":
                    prause(f"YOU ATTACK ENEMY -{sword_crit_chance}")

                    enemyhp -= sword_crit_chance

                    prause(f"ENEMY HP:{enemyhp}")

                    yourturn -= 1

                    joeturn += 1

            if decide == "b" or decide == "B":
                hp += 10

                yourturn -= 1

                joeturn += 1

        elif joeturn == 1:
            prause("ITS JOE'S TURN")

            prause(f"JOE CHOOSES to{joes_choose_chance}")

            if joes_choose_chance == "attack":
                prause(f"JOE ATTACKS -{joes_crit_chance}")

                enemyhp -= joes_crit_chance

                joeturn -= 1

                enemyturn += 1

            elif joes_choose_chance == "defend":
                prause(f"JOE DEFENDS")

                joehp += 10

                joeturn -= 1

                enemyturn += 1

        elif enemyturn == 1:
            if enemy == "moth" and enemychoose_chance == "you":
                prause(f"THE ENEMY ATTACKS YOU -{moth_crit_chance} ")

                hp -= moth_crit_chance

                print(f"YOUR HP NOW IS {hp}")

            elif enemy == "moth" and enemychoose_chance == "joe":
                prause(f"THE ENEMY ATTACKS JOE -{moth_crit_chance}")

                joehp -= moth_crit_chance

                print(f"JOES HP NOW IS {joehp}")

            elif enemy == "achoo" and enemychoose_chance == "you":
                prause(f"THE ENEMY ATTACKS YOU -{achoo_crit_damage}")

                hp -= achoo_crit_damage

                print(f"YOUR HP NOW IS {hp}")

            elif enemy == "achoo" and enemychoose_chance == "joe":
                prause(f"THE ENEMY ATTACKS JOE -{achoo_crit_damage}")

                joehp -= achoo_crit_damage

                prause(f"JOES HP IS NOW {joehp}")

            elif enemy == "gopro" and enemychoose_chance == "you":
                prause(f"THE ENEMY ATTACKS YOU -{gopro_crit_damage}")

                print(f"YOUR HP NOW IS {hp}")

                hp -= gopro_crit_damage

            elif enemy == "gopro" and enemychoose_chance == "joe":
                prause(f"THE ENEMY ATTACKS JOE -{gopro_crit_damage}")

                joehp -= gopro_crit_damage

                prause(f"JOES HP IS NOW {joehp}")

            enemyturn -= 1

            yourturn += 1

    if hp <= 0 and joehp <= 0:
        retrytime_record()

    elif enemyhp <= 0:
        print("YOU WIN")


# now to the start of the game

prause("you are in the middle of a forest with some friends(paid actors)")

prause("you make a camp and then you play a game of truth or dare")

prause("you get dared to sleep in the cave 2 miles away from the camp")

prause(
    "if you didnt accept the dare, you'll pay for whatever they want for the next month"
)

prause("so you go with 2 sandwiches")

prause("you enter the cave")

prause("you trip into a hole....")

prause("a big one")

print("long ago two races ruled the world: monsters and humans-")

prause("oh sorry wrong game")

hunger -= 40

hp -= 30

score += 5

prause("you wake up and you're hurt and hungry")

pressed = False
while not pressed:
    q = input(
        "so would you eat a sandwich(heals 30 hp and increases hunger by 40 p)Y/N"
    )

    if q == "Y" or q == "y":
        pressed == True

        prause("you eat the sandwich")

        hp == 100

        hunger == 100

        score += 10

        inventory["sandwich"] -= 1

        pressed == False

        prause("refreshing")

        prause("you continue your way")

        prause("you feel a strange aura")

        prause("you see a shadow of something human like")

        w = input("would you A) scream or B) look for a weapon")

        while not pressed:
            if w == "A" or w == "a":
                pressed == True

                prause("you scream")

                score += 5

                prause("the moster gets afraid and instantly kills you")

                retrytime_record()

            elif w == "b" or w == "B":
                pressed == True

                prause("you look for a weapon")

                prause("you find a broom")

                score += 10

                pressed == False

                weapon["broom"] += 1

                prause("you grab the broom and ready yourself for a fight")

                prause("the monster sees you and understands your fear")

                prause("the monster gets out of the shadow and its a fish-human thing")

                prause("he introduces himself as joe")

                prause("joe tells you to not say that stupid joke")

                e = input("so would you say it or not Y/N")

                while not pressed:
                    if e == "y" or e == "Y":
                        pressed == True

                        prause("joe gets angry AND HE WILL NOT LEAVE YOU TILL YOU DIE")

                        prause("FIGHTMODE ENGAGED")

                        prause("JOE ATTACKS YOUR HP - 400")

                        retrytime_record()

                    elif e == "n" or e == "N":
                        pressed == True

                        prause("joe is happy to meet you and now he joins the party")

                        prause("you continue your way to find the exit")

                        prause("a bodybuilder sized mothe aproaches")

                        FIGHTMODE("broom", "moth")

                        score += 20
                       
                        hp == 100

                        joehp == 400

                        prause("that was easy")

                        prause("you continue your way")

                        pressed == False

                        while not pressed:
                            r = input("you find a bow would you take it? Y/N")

                            if r == "y" or r == "Y":
                                
                                del weapon["broom"] 

                                weapon["bow"] += 1

                                pressed == True

                                prause("you get the bow")

                                score += 30

                                pressed == False
                                
                                prause(
                                    "YOUR ATTACK INCREASES AND YOUR DEFENSE INCREASES BY MAGIC OF 'take this you lucky guy'"
                                )

                                hp == 200

                                prause("you continue and find a yellow ra from pokeyman called achoo")

                                FIGHTMODE("bow","achoo")

                                score += 30
                               
                                prause("ah finally we finished this long battle also why did joe defend so much")

                                prause("you continue and find a glowing cave")

                                prause("you and joe get inside")

                                prause("OH MY GOD ITS THE SWORD FROM DOOM ITS SO OP BRO")

                                prause("joe is very happy and he tells you to take it")

                                prause("ATTACK INCREASES AND DEFENSE INCREASES")

                                hp == 500

                                score += 50
                               
                                prause("you and joe continue till you find the final exit from this creppy cave")

                                prause("you aproach it...")

                                print("slow")

                                tm.sleep(4)

                                prause("and steady while making yourself ready for an upcoming fight")

                                prause("you feel it in your guts")

                                prause("youre 4ft away from the door")

                                prause("THE BLUE GOPRO FROM ULTRAKILL LANDS INFRONT OF YOU")

                                FIGHTMODE("sword", "gopro")

                                score += 100
                                prause("YEEEES LES GOOOOO")

                                prause("you and joe get out")

                                prause("joe disguises as a human and you become friends with him till eternity")

                                et = tm.time()

                                el = et - s

                                d = dtm.timedelta(seconds=el)

                                dstr = str(d)

                                print(F"YOU WIN YOUR SCORE IS {score} AND YOU FINISHED IN {dstr}")

                                sys.exit(1)

                            elif r == "n" or r == "N":
                                print("you dont take the bow")

                                prause("G-man: prepare for unforseen consequences")

                                prause("gordon freeman jumps out of a portal and yeets you with his portal gun")

                                retrytime_record()

    elif q == "N" or q == "n":
        pressed == True

        prause("you dont eat the sandwich")

        prause("you feel so hurt that you cant even move")

        prause("a big rock falls on you and crushes you")

        prause("you're now her crush lol")

        retrytime_record()
